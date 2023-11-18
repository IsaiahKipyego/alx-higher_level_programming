#!/usr/bin/python3
"""script retrieves and prints all cities along with MySQL database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":

    # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creates engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Creates all tables if they don't exist
    Base.metadata.create_all(engine)

    # Creates a configured Session class
    Session = sessionmaker(bind=engine)

    # Creates a session
    session = Session()

    # Query all City objects and their associated State objects
    cities = session.query(City).join(State).order_by(City.id)

    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
