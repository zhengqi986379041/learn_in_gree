from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.dir_config import screenshot_dir
import logging
import datetime
from time import strftime,localtime


class BasePage:
    """
    封装基本函数-执行日志、异常处理、失败截图
    所有的页面公共的部分
    """
    def __init__(self, driver):
        self.driver = driver


    def wait_eleVisible(self, locator, wait_times = 30, doc = ""):
        """
        等待元素可见

        :param locator:元素定位
        :param times:默认等待时长
        :param poll_frequency:等待间隔
        :return:
        """
        logging.info("等待元素{0}可见".format(locator))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            logging.getLogger().setLevel(logging.INFO)
            logging.info("等待结束，等待时长为：{0}s".format((end - start).seconds))
            # print("print:等待元素{0}结束，等待时长为：{1}s".format(locator, (end - start).seconds))
        except:
            logging.exception("等待元素可见失败！")
            self.save_screenshots(doc)
            raise


    def wait_elePresence(self):
        """
        等待元素存在
        :return:
        """
        pass

    def get_element(self, locator, doc = ""):

        logging.info("查找元素：{0}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！")
            self.save_screenshots(doc)
            raise

    def click_element(self, locator, doc = ""):
        """
        点击操作
        :param locator: 元素
        :param doc: 模块名_页面名称_操作名称
        :return: None
        """
        ele = self.get_element(locator, doc)
        logging.info("{0}点击元素：{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("点击元素操作失败！")
            self.save_screenshots(doc)
            raise

    def b_back(self):
        logging.info("浏览器返回操作~")
        self.driver.back()

    def input_text(self, locator, text, doc = ""):
        """
        输入操作
        :param locator:
        :param text:
        :param doc:
        :return:
        """
        ele = self.get_element(locator, doc)
        logging.info("{0}操作元素：{1}输入内容：{2}".format(doc, locator, text))
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败！")
            self.save_screenshots(doc)
            raise

    def clear_text(self, locator, doc = ""):
        ele = self.get_element(locator, doc)
        logging.info("{0}操作元素：{1}清空内容".format(doc, locator))
        try:
            ele.clear()
        except:
            logging.exception("元素清除操作失败！")
            self.save_screenshots(doc)
            raise


    def get_text(self, locator, doc = ""):
        """
        获取元素文本
        :param locator:
        :param doc:
        :return:
        """
        ele = self.get_element(locator, doc)
        logging.info("{0}获取元素：{1}的文本".format(doc, locator))
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！")
            self.save_screenshots(doc)
            raise

    def get_element_attribute(self, locator, attr, doc = ""):
        """
        获取元素属性
        :param locator:
        :param attr:
        :param doc:
        :return:
        """
        ele = self.get_element(locator, doc)
        logging.info("{0}获取元素：{1}的属性".format(doc, locator))
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素属性失败！")
            self.save_screenshots(doc)
            raise

    def alert_action(self, action = 'accept'):
        """
        alert处理
        :param action:
        :return:
        """
        pass

    def switch_iframe(self, iframe_reference):
        """
        iframe切换
        :param iframe_reference:
        :return:
        """
        pass

    def upload_file(self):
        """
        上传操作
        :return:
        """
        pass

    # 滚动条处理
    def scroll_to_see(self, locator, doc = ""):
        ele = self.get_element(locator, doc)
        logging.info("查找元素{0}".format(locator))
        try:
            js4 = "arguments[0].scrollIntoView(false);"
            self.driver.execute_script(js4, ele)
        except:
            logging.exception("下拉查找元素失败！")
            self.save_screenshots(doc)
            raise
    def scroll_to_bottom(self, doc = ""):
        logging.info("拖拽底部")
        try:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        except:
            logging.exception("拖拽底部失败！")
            self.save_screenshots(doc)
            raise
    # 窗口切换

    # 查找列表元素个数
    def number_of_list_elements(self, locator, doc = ""):
        eles = self.driver.find_elements_by_xpath(locator[1])
        logging.info("查找列表元素个数为{0}".format(len(eles)))
        print(logging.info("查找列表元素个数为{0}".format(len(eles))))
        return len(eles)


    # 截图
    def save_screenshots(self, doc):
        # 图片名称 ：模块名_页面名称_操作名称_年-月-日_时分秒.png
        filePath = screenshot_dir + "/{0}_{1}.png".format(doc, strftime("%Y-%m-%d_%H-%M-%S", localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截取网页成功，文件路径为：{0}".format(filePath))
        except:
            logging.exception("截图失败！")