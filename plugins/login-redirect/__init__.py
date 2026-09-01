""" Auto-redirect /login to the SSO provider login """

from flask import redirect, request

SSO_CLIENT_ID = 2


def load(app):
    @app.before_request
    def redirect_login_to_sso():
        if request.method == "GET" and request.path == "/login":
            return redirect("/sso/login/{}".format(SSO_CLIENT_ID))
