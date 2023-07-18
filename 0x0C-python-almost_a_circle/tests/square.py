import unittest
from models.square import Square


class SquareTest(unittest.TestCase):
    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            s.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_str(self):
        s = Square(4, 1, 2, 10)
        expected_str = "[Square] (10) 1/2 - 4"
        self.assertEqual(str(s), expected_str)


if __name__ == "__main__":
    unittest.main()
