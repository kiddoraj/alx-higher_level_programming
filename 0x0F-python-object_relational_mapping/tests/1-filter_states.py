import unittest
from unittest.mock import patch
import io
import 1-filter_states.py  # Import the script to be tested

class TestListStatesWithNScript(unittest.TestCase):

    @patch('sys.argv', ['list_states_with_N.py', 'test_user', 'test_password', 'test_db'])
    def test_list_states_with_N(self):
        # Redirect stdout to capture the script's output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Run the script
        list_states_with_N.main()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the captured output
        output_lines = captured_output.getvalue().strip().split('\n')

        # Check if the output contains at least one state name starting with 'N'
        self.assertTrue(any("N" in line for line in output_lines))

if __name__ == '__main__':
    unittest.main()
