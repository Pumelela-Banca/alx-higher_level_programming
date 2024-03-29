#!/usr/bin/python3

"""
lists State with same name as passed in object
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
    state = states.filter(State.name == sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
