#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    try:
        us = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]

        engine = \
            create_engine(f"mysql+mysqldb://{us}:{pwd}@localhost/{db}")
        Base.metadata.create_all(engine)
        Session = sessionmaker()
        local_session = Session(bind=engine)
        Califonia = State(name='California',
                          cities=[(City(name='San Francisco'))])
        local_session.add(Califonia)
        local_session.commit()
    except Exception as e:
        print(f"Error: {e}")