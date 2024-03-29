#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    try:
        us = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]
        engine = create_engine(f"mysql+mysqldb://{us}: {pwd}@localhost/{db}",
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker()
        local_session = Session(bind=engine)
        users = local_session.query(State).first()
        if users:
            print("{}: {}".format(users.id, users.name))
        else:
            print("Nothing\n")

        local_session.close()
    except Exception as e:
        print(f"Error: {e}")
