#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_city import City
from relationship_state import  Base
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
        cities = local_session.query(City).order_by(City.id).all()
        for city in cities:
            state = city.states
            print(f"{city.id}: {city.name} -> {state.name}")
        local_session.commit()
    except Exception as e:
        print(f"Error: {e}")