# -*-coding:utf-8-*-

from karlooper.web.application import Application
from karlooper.web.request import Request
from karlooper.utils.parse_command_line import CommandLineParser
from test import test_handler
import os

__author__ = 'karlvorndoenitz@gmail.com'


class TestHandler(Request):
    def get(self):
        test = self.get_parameter("test")
        cookie = self.get_cookie("what1")
        cookie_1 = self.get_security_cookie("what")
        result = {
            "key": "value",
            "test": test,
            "cookie": cookie,
            "cookie_1": cookie_1
        }
        http_message = self.get_http_request_message()
        self.set_header({
            "what": "happened",
            "hello": "world",
            "ok": "let's go"
        })
        self.clear_header("ok")
        print http_message
        self.set_security_cookie("what", "happened")
        self.set_security_cookie("what", "are you")
        self.set_cookie("what1", "happened1")
        self.set_cookie("what2", "happened2")
        return self.response_as_json(result)

    def post(self):
        http_message = self.get_http_request_message()
        print http_message
        post_1 = self.get_parameter("post1")
        result = {
            "key": "value",
            "test": 7758521,
            "post1": post_1
        }
        self.set_cookie("what", "happened")
        return self.response_as_json(result)


class TestHandler2(Request):
    def get(self):
        result = {
            "k": "v"
        }
        return self.response_as_json(result)
        # return self.redirect("http://www.baidu.com")


class Document(Request):
    def get(self):
        f = open("/opt/zhihao/bpi_api/static/bpi_api_document.md")
        # f = open("/Users/lizhihao/Downloads/my pdf/python_source_code_analy.pdf")
        # f = open("/Users/lizhihao/PycharmProjects/karlooper/document.md")
        data = f.read()
        f.close()
        self.set_header({"Content-Type": "text/plain"})
        # self.set_header({"Content-Type": "application/octet-stream"})
        return data


class Hello(object):
    pass


class HelloWorld(Request):
    def get(self):
        title = "你好, 世界"
        numbers = [1, 2, 3, 4, 5]
        hello = Hello()
        hello.world = "world"
        return self.render("/helloworld.html", title=title, numbers=numbers, hello=hello)


handlers = {
    "/test": TestHandler,
    "/test/test2": TestHandler2,
    "/document.md": Document,
    "/hello": HelloWorld,
    "/test-handler": test_handler.TestHandler1
}


settings = {
    "template": os.getcwd() + "/template",
    "static": os.getcwd() + "/template",
    "log_enable": False
}


if __name__ == '__main__':
    CommandLineParser.default(port=9987, log_enable=False)
    CommandLineParser.parse_command_line()
    application = Application(handlers, settings)
    application.run()
