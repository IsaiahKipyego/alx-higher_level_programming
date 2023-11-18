#!/usr/bin/python3
"""script that adds a city and its associated state\
    to a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creates database tables based on defined models
    Base.metadata.create_all(engine)

    # Creates a session factory
    Session = sessionmaker(bind=engine)

    # Creates a session object
    session = Session()

    # Creates a new city and its associated state
    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # Adds new city and associated state to session
    session.add(state)
    session.add(city)

    # Commits session to persist changes in database
    session.commit()

0x0F-python-object_relational_mapping/100-relationship_states_cities.sql

-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

SELECT * FROM states;
SELECT * FROM cities;
