import unittest
from unittest.mock import patch
import io
import 3-my_safe_filter_states.py  # Import the script to be tested

class TestFindStateSafeScript(unittest.TestCase):

    @patch('sys.argv', ['find_state_safe.py', 'test_user', 'test_password', 'test_db', 'California'])
    def test_find_state_safe(self):
        # Redirect stdout to capture the script's output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Run the script
        find_state_safe.main()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the captured output
        output_lines = captured_output.getvalue().strip().split('\n')

        # Check if the output contains at least one line with the searched state name
        self.assertTrue(any("California" in line for line in output_lines))

if __name__ == '__main__':
    unittest.main()
