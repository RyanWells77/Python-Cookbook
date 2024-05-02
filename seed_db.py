
from flask import Flask
from model import db, connect_to_db
from server import app

def drop_tables():
    db.drop_all()

def create_tables():
    db.create_all()

if __name__ == '__main__':
    connect_to_db(app)

    drop_tables()
    create_tables()

    print("Database dropped and recreated.")
