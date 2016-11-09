#!/usr/bin/env python
# coding=utf-8
from handlers.book import BookHandler
from handlers.book_edit import BookEditHandler
from handlers.login import LoginHandler
from handlers.recommended import RecommendedHandler


def get_routes():
    routes = [

        # urls
        (r"/", LoginHandler),
        (r"/recommended/", RecommendedHandler),
        (r"/books/([0-9Xx\-]+)", BookHandler),
        (r"/edit/([0-9Xx\-]+)", BookEditHandler),
        (r"/add", BookEditHandler),

        # Auth
        # (r"/auth/login", LoginHandler),
        # (r"/auth/logout", LogoutHandler),
        # (r"/auth/register", RegisterHandler)

    ]

    return routes
