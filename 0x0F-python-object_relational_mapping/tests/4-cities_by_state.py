import unittest
from unittest.mock import patch
import io
import 4-cities_by_state.py # Import the script to be tested

class TestListCitiesScript(unittest.TestCase):

    @patch('sys.argv', ['list_cities.py', 'test_user', 'test_password', 'test_db'])
    def test_list_cities(self):
        # Redirect stdout to capture the script's output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Run the script
        list_cities.main()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the captured output
        output_lines = captured_output.getvalue().strip().split('\n')

        # Check if the output contains at least one line with city data (assuming the database has data)
        self.assertTrue(any("City Data" in line for line in output_lines))

if __name__ == '__main__':
    unittest.main()
