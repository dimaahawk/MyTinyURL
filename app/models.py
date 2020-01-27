from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'Url(token={self.token})'

    @classmethod
    def by_token(cls, token):
        return cls.query.filter_by(
            token=token
        ).one()
