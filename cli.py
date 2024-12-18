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

def update_event():
    event_id = int(input("Enter Event ID to update: "))     
    event = session.get(Event, event_id)
    if not event:
        print(f"Event with ID {event_id} does not exist")
        return
    event.name = input("Enter new name for event(current: {event.name}): ") or event.name  
    event.location = input("Enter new location for event(current: {event.location}): ") or event.location
    event.description= input("Enter new description for event(current: {event.description}): ") or event.description 
    new_school_id = input(f"Enter new School ID for event(current: {event.school_id})") or event.school_id
    if new_school_id:
        new_school = session.get(School, int(new_school_id))
        if not new_school:
            print(f"School with ID {new_school_id} does not exist. Skipping School update. ")
        else:
            event.school_id = new_school_id
    session.commit()
    print(f"Event ID {event_id} updated successfully")

def delete_event():
    event_id = int(input("Enter event id to delete: "))
    event = session.get(Event, event_id)  
    if not event:
        print(f"Event with ID {event_id} does not exist")
        return              
    session.delete(event)
    session.commit()
    print(f"Event ID {event_id} deleted successfully")

def assign_event():
    event_id = int(input("Enter Event ID: "))    
    school_id = int(input("Enter the new School ID: "))
    event = session.get(Event, event_id)
    school = session.get(School, school_id)
    if not event or not school:
        print(f"Invalid event Id or School Id.")
        return
    event.school_id = school_id
    session.commit()
    print("School assignrd successfully")
    