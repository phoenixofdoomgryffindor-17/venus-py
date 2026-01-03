from pages import home, login, signup, marketplace, write, settings, support, book

ROUTES = {
    "home": home,
    "login": login,
    "signup": signup,
    "marketplace": marketplace,
    "write": write,
    "settings": settings,
    "support": support,
    "book": book,
}

class Router:
    def __init__(self, view):
        self.view = view

    def go(self, route, **params):
        page = ROUTES[route]
        html = page.render(**params)
        self.view.load_html(html)
