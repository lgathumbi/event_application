import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, School, Event

DATABASE_URL = "sqlite:///schools.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind= engine)
session = Session()

def init_db():
    #intialize database
    Base.metabase.create_all(engine)
    print("Database Initialized")

def create_school():
    name = input("Enter School name")
    email = input("Enter School email")
    address = input("Enter School address")
    school = School(name = name, email = email, address = address)
    session.add(school)
    session.commit()
    print(f"School '{name}' craeted with ID {school.id}")

def update_school():
    school_id = int(input("Enter School ID to update"))
    school = session.get(school_id)
    if not school:
        print(f"School with ID {school_id} does not exist")
        return
    school.name = input(f"Enter new name for School(current:{school.name}): ") or school.name
    school.email = input(f"Enter new email for School(current:{school.email}): ") or school.email
    session.commit()
    print(f"School ID {school_id} update successfully")

def delete_school():
    school_id = int(input("Enter School ID to delete: "))
    school = session.get(School, school_id)
    if not school:
        print(f"School with ID {school_id} does not exist.") 
        return
    session.delete(school)
    session.commit()
    print(f"School ID {school_id} deleted successfully")

def create_event():
    name = input("Enter event name: ")
    location = input("Enter event location: ")
    description = input("Enter event description: ")
    school_id = int(input("Enter School ID: "))   
    school = session.get(School, school_id)
    if not school:
        print(f"School with ID {school_id} does not exist") 
        return
    event = Event(name = name, location = location, description = description)
    session.add(event)
    session.commit()
    print(f"Event '{name}' craeted with ID {event.id} and assigned to School_ID {school_id}")
     