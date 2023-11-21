#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import City, Base
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import desc

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
        cities = local_session.query(City, State).join(State).order_by(City.id).all()
        for city, state in cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    except Exception as e:
        print(f"Error: {e}")