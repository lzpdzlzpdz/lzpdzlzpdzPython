import time
import logging
import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
import  datetime

import functools
from tornado import stack_context

tornado.options.parse_command_line()


def my_asynchronous(method):
    from tornado.ioloop import IOLoop

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._auto_finish = False
        with stack_context.ExceptionStackContext(
                self._stack_context_handle_exception):
            result = method(self, *args, **kwargs)
            if result is not None:
                result = gen.convert_yielded(result)

                def future_complete(f):
                    f.result()
                    if not self._finished:
                        self.finish()
                IOLoop.current().add_future(result, future_complete)
                return None
            return result
    return wrapper


class MainHandler(tornado.web.RequestHandler):
    @my_asynchronous
    def get(self):
        self.write("Hello, world")
        self.finish()


class NoBlockingHnadler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(10)
        print 'NoBlockingHnadler',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.write('NoBlockingHnadler Request')


class BlockingHnadler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        time.sleep(10)
        print 'BlockingHnadler',datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.write('Blocking Request')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/block", BlockingHnadler),
        (r"/noblock", NoBlockingHnadler),
    ], autoreload=True)


if __name__ == "__main__":
    app = make_app()
    port = 8001
    app.listen(port)
    print '127.0.0.1:%s' % port
    tornado.ioloop.IOLoop.current().start()

