from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

# read the csv files to create the data you will need to create the players
# hint: pandas

# add and commit the players, teams, sports and cities below
