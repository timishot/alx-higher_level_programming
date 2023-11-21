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
        user_to_update= local_session.query(State).filter(State.id==2).first()
        user_to_update.name = "New Mexico"
        local_session.commit()
        
    except Exception as e:
        print(f"Error: {e}")