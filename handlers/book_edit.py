import tornado
from tornado import gen


class BookEditHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, isbn=None):
        book = dict()
        if isbn:
            coll = self.application.db.books
            book = yield coll.find_one({"isbn": isbn})
        self.render("book_edit.html",
                    page_title="Books",
                    header_text="Edit book",
                    book=book)

    @gen.coroutine
    def post(self, isbn=None):
        import time
        book = dict()
        book_fields = ['isbn', 'title', 'subtitle', 'image', 'author',
                       'date_released', 'description']
        coll = self.application.db.books
        if isbn:
            book = yield coll.find_one({"isbn": isbn})
        for key in book_fields:
            book[key] = self.get_argument(key, None)

        if isbn:
            yield coll.save(book)
        else:
            book['date_added'] = int(time.time())
            yield coll.insert(book)
        self.redirect("/recommended/")