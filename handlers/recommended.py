import tornado
from tornado import gen


class RecommendedHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        coll = self.application.db.books
        books = yield coll.find({}).to_list(length=5)

        self.render(
            "recommended.html",
            page_title="Books | Recommended Reading",
            header_text="Recommended Reading",
            books=books
        )
