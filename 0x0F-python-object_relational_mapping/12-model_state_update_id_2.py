#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Create a database engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name))

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the State object with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()

        # Check if the state with id = 2 exists
        if state_to_update:
            # Update the name to "New Mexico"
            state_to_update.name = "New Mexico"
            session.commit()  # Commit the transaction to save the changes
        else:
            print("State with id 2 not found")

    except Exception as e:
        print("Error: {}".format(e))
    finally:
        if session:
            session.close()
