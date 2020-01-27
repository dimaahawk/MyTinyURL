from flask import request
from flask import redirect
from flask.views import MethodView
from app.models import Url
from app.models import db


class Main(MethodView):

    def get(self):
        return 'ok'

    def post(self):
        token, url = request.form.get('token'), request.form.get('url')
        new = Url(token=token, url=url)
        db.session.add(new)
        db.session.commit()
        return f'Created: {token} -> {url}'


class Retrieve(MethodView):

    def get(self, token):
        result = Url.by_token(token)
        return redirect(result.url)
        