#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Create a database engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name))

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the State object with the specified name
        state = session.query(State).filter_by(name=state_name).first()

        # Display the result or "Not found" if no state with the given name exists
        if state is None:
            print("Not found")
        else:
            print(state.id)

    except Exception as e:
        print("Error: {}".format(e))
    finally:
        if session:
            session.close()
