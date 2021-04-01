import re
import pymysql


class DoMysql:
    @staticmethod
    def get_conn():
        conn = pymysql.connect(host='121.37.248.126', port=4406, user='root', passwd='Gree@2020',
                               database="basecenter")  # db:表示数据库名称
        return conn

    @staticmethod
    def query(sql):
        conn = DoMysql.get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        # print(type(results))  # 返回<class 'tuple'> tuple元组类型
        # print(results[0][3])
        # a = results[0][3]
        # a = re.findall(r'{.*?}', results[0][3])
        # print(a)
        # print(int(a[0].strip('{}')))
        # print(re.findall(r"\d+\.?\d*", results[0][3])[0])
        return re.findall(r"\d+\.?\d*", results[0][3])[0]
        conn.commit()
        cur.close()
        conn.close()
if __name__ == '__main__':#16626272288 18285050813
    sql = 'SELECT * FROM basecenter.base_send_message where address = "16626272288" order by id desc limit 1;'
    # query(sql,None)
    b = DoMysql.query(sql)
    print(b)
