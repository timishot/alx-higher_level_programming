#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
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
        new_users = State(name='Louisiana')
        local_session.add(new_users)
        local_session.commit()
        list_user=local_session.query(State).order_by(State.id.desc()).first()
        if list_user:
            print(list_user.id)
        else:
            print("Not found")
    except Exception as e:
        print(f"Error: {e}")