from app import db, Users, People

db.drop_all()
db.create_all()

testuser = Users(first_name='Grooty',last_name='Toot') # Extra: this section populates the table with an example entry
testperson = People(name='Erhan', height='1.80')

db.session.add(testperson)
db.session.add(testuser)
db.session.commit()