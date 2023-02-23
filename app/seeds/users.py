from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    brandon = User(
        username='Brandon', email='brandonjshin98@gmail.com', password='password')
    joon = User(
        username='Joon', email='joonlee8983@gmail.com', password='password')
    fred = User(
        username='Fred', email='fred.jeong16@gmail.com', password='password')
    christina = User(
        username='Christina', email='phung.christina16@gmail.com', password='password')

    db.session.add(brandon)
    db.session.add(joon)
    db.session.add(fred)
    db.session.add(christina)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
