import tornado


class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string(
            "modules/book.html",
            book=book,
        )

    def css_files(self):
        return "css/recommended.css"

    def javascript_files(self):
        return 'js/recommended.js'
