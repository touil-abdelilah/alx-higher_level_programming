#!/usr/bin/python3
"""Script to print the State object with the name passed as argument
    from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State object with the provided state name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
