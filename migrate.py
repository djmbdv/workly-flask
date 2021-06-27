from app import db
from models import User
from werkzeug.security import generate_password_hash
admin = User(username='admin',password=generate_password_hash("holamundo") ,email='admin@example.com')
guest = User(username='guest', password=generate_password_hash("test") ,email='guest@example.com')
db.drop_all()
db.create_all()
db.session.add(admin)
db.session.add(guest)
db.session.commit()