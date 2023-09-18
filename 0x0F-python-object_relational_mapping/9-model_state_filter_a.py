#!/usr/bin/python3

"""
lists first State all state objects with letter
a
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        """mysql+mysqldb://{}:{}@localhost:3306/{}""".
        format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for a in states:
        if "a" in a.name:
            print(f"{a.id}: {a.name}")
