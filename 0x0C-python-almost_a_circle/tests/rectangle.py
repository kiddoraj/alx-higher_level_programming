import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 3)
        expected_output = "###\n###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 10)
        expected_str = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(r), expected_str)


if __name__ == "__main__":
    unittest.main()
