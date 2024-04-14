#!/usr/bin/python3
"""Script to create a State with a City from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    new_state = State(name='California')

    # Add the State to the session
    session.add(new_state)

    # Commit the changes
    session.commit()

    # Create a new City object linked to the State
    new_city = City(name='San Francisco', state=new_state)

    # Add the City to the session
    session.add(new_city)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
