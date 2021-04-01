import pymysql
import re

# 获取连接对象conn，建立数据库的连接
def get_conn():
    conn = pymysql.connect(host='121.37.248.126',port=4406,user='root',passwd='Gree@2020', database="basecenter")    # db:表示数据库名称
    return conn
def query(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    # print(type(results))  # 返回<class 'tuple'> tuple元组类型
    # print(results)
    for row in results:
        # print(row)
        id = row[0]
        address = row[1]
        content = row[3]
        # print(str(content).split('：')[1].split('，')[0])
        print('id:' + str(id) + ' address:' + address + ' content:' + str(content))
        print(re.findall(r"\d+\.?\d*", content)[0])
        pass

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    sql = 'SELECT * FROM basecenter.base_send_message where address = "16626272288" order by id desc limit 1;'
    query(sql,None)
