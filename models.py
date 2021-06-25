from app import db,ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(120),nullable=True)
    def __repr__(self):
        return '<User %r>' % self.username



class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "username", "location", "id")

user_schema = UserSchema()
users_schema = UserSchema(many=True)