import tornado


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title="Books | Home",
            header_text="Welcome to Base Project!",
        )