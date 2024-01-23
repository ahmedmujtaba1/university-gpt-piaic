from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

DeclarativeBase = declarative_base()

def mapped_column(*args, **kwargs):
    return Column(*args, **kwargs)

## USER (CLASSES) ---------------------------------------------
class Student(DeclarativeBase):
    __tablename__ = 'universities_student'
    studentID = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    mobile_number = Column(String)
    name = Column(String)

class Instructor(DeclarativeBase):
    __tablename__ = 'universities_instructor'
    instructorID = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    mobile_number = Column(String)
    name = Column(String)

## TOPIC (Classes) --------------------------------------------
class Topic(DeclarativeBase):
    __tablename__ = 'topics'
    id = Column(String, primary_key=True)
    title = Column(String)
    desc = Column(Text)
    parent_id = Column(String, ForeignKey('topics.id'))
    subtopics = relationship("Topic", backref=backref("parent", remote_side=[id]))

class Question(DeclarativeBase):
    __tablename__ = 'questions'
    id = Column(String, primary_key=True)
    topic_id = Column(String, ForeignKey('topics.id'))
    title = Column(String)
    text = Column(Text)
    points = Column(Integer)
    type = Column(String) 

class MCQ(Question):
    __tablename__ = 'mcqs'
    id = Column(String, ForeignKey('questions.id'), primary_key=True)
    question_bank_id = Column(String)
    options = relationship("Option", backref="mcq")

class Option(DeclarativeBase):
    __tablename__ = 'options'
    id = Column(String, primary_key=True)
    mcq_id = Column(String, ForeignKey('mcqs.id'))
    text = Column(Text)
    correct = Column(Boolean)
 
## UNIVERSITY BASIC (MODELS) -----------------------------------
class University(DeclarativeBase):
    __tablename__ = 'universities'  
    id = Column(String, primary_key=True)  
    name = Column(String, nullable=False)
    programs = relationship("Program", backref="university")

class Program(DeclarativeBase):
    __tablename__ = 'programs'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    university_id = Column(String, ForeignKey('universities.id'))
    courses = relationship("Course", backref="program", passive_deletes=True)

    def __repr__(self) -> str:
        return f"<Program {self.name}>"

class Course(DeclarativeBase):
    __tablename__ = 'courses'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    program_id = mapped_column(Integer, ForeignKey('programs.id', ondelete="CASCADE"))

    def __repr__(self) -> str:
        return f"<Course {self.name}>"

engine = create_engine('postgresql://ahmedmujtaba1:1bKOzMiEgQV9@ep-noisy-surf-36032677.us-east-2.aws.neon.tech/todo?sslmode=require')
DeclarativeBase.metadata.create_all(engine)