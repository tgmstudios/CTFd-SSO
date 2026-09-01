""" Auto-redirect /login and /register to the SSO provider login """

from flask import redirect, request

SSO_CLIENT_ID = 2
REDIRECT_PATHS = ("/login", "/register")


def load(app):
    @app.before_request
    def redirect_login_to_sso():
        if request.method == "GET" and request.path in REDIRECT_PATHS:
            return redirect("/sso/login/{}".format(SSO_CLIENT_ID))
