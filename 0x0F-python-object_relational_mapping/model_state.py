#!/usr/bin/python3
"""Start link class to table in the database
"""

import sys
from model_state import Base, State  # Import necessary modules and classes

from sqlalchemy import create_engine  # Import the create_engine function

if __name__ == "__main__":
    # Create a database engine using SQLAlchemy
    # The connection URL is constructed from command-line arguments: username, password, and database name
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table in the database that corresponds to the State class
    Base.metadata.create_all(engine)
