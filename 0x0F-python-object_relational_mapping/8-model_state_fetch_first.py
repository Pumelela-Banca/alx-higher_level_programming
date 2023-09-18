#!/usr/bin/python3

"""
lists first State object from the database hbtn_0e_6_usa
and prints it, prints Nothing if table empty
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
    states = session.query(State).order_by(State.id).first()
    if states is None:
        print("Nothing")
    else:
        print(f"{states.id}: {states.name}")
