import tornado
from tornado import gen


class BookHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, isbn=None):
        if isbn:
            coll = self.application.db.books
            book =yield coll.find_one({"isbn": isbn})
            if book:
                self.render("one_book.html",
                            page_title="Books | " + book['title'],
                            header_text=book['title'],
                            book=book)
                return
        self.set_header(404)
        return