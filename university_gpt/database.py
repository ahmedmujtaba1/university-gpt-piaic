from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

DeclarativeBase = declarative_base()

def mapped_column(*args, **kwargs):
    return Column(*args, **kwargs)

class Program(DeclarativeBase):
    __tablename__ = 'programs'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    years_of_study = mapped_column(Integer, nullable=False)
    courses = relationship("Course", backref="program", passive_deletes=True)

    def __repr__(self) -> str:
        return f"<Program {self.name}>"

class Course(DeclarativeBase):
    __tablename__ = 'courses'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    program_id = mapped_column(Integer, ForeignKey('programs.id', ondelete="CASCADE"))
    # Other fields and relationships

    def __repr__(self) -> str:
        return f"<Course {self.name}>"

engine = create_engine('postgresql://ahmedmujtaba1:1bKOzMiEgQV9@ep-noisy-surf-36032677.us-east-2.aws.neon.tech/todo?sslmode=require')
DeclarativeBase.metadata.create_all(engine)