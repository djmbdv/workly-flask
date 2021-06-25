from app import db
from models import User
admin = User(username='admin',password="holamundo" ,email='admin@example.com')
guest = User(username='guest', password="test" ,email='guest@example.com')
db.drop_all()
db.create_all()
db.session.add(admin)
db.session.add(guest)
db.session.commit()