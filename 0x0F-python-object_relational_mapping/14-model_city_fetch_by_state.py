#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State

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

        # Query all City objects sorted by id
        cities = session.query(City).order_by(City.id).all()

        # Display the results in the required format
        for city in cities:
            state_name = session.query(State).filter_by(id=city.state_id).first().name
            print("{}: ({}) {}".format(state_name, city.id, city.name))

    except Exception as e:
        print("Error: {}".format(e))
    finally:
        if session:
            session.close()
