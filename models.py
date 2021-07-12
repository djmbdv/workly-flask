from app import db,ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=True)
    password = db.Column(db.String(120),nullable=True)
    certificates = db.relationship('Certificate', lazy='select',
        backref=db.backref('user', lazy='joined'))
    skills = addresses = db.relationship('Skill', lazy='select',
        backref=db.backref('user', lazy='joined'))
    def __repr__(self):
        return '<User %r>' % self.username


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    type_skil_id = db.Column(db.Integer, db.ForeignKey('person.id'))


class TipeSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer,nullable=False)

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "username", "location", "id")

user_schema = UserSchema()
users_schema = UserSchema(many=True)