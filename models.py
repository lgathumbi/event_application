from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String, unique=True, nullable= False)

    events = relationship("Event",back_populates="school")

    def __repr__(self):
        return f"School(id = {self.id}, name = '{self.name}', email ='{self.email}', address ='{self.address}')"
    
class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)    
    name = Column(String, nullable=False)
    location = Column(String, unique=True, nullable=False)
    description = Column(String, unique=True, nullable=False)
    school_id = Column(Integer, ForeignKey('schools.id'))

    school = relationship("School", back_populates="events")

    def __repr__(self):
        return f"Event(id = {self.id}, name ='{self.name}', location ='{self.location}', description ='{self.description}', school_id ={self.school_id})"
