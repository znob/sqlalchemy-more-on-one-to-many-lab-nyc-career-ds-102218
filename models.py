from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Player, City, Sport and Team tables below







engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)
