import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    def test_init_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_init_custom_id(self):
        b2 = Base(10)
        self.assertEqual(b2.id, 10)

    def test_to_json_string(self):
        b1 = Base(1)
        b2 = Base(2)
        expected_json = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()]), expected_json)

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        expected_data = [{"id": 1}, {"id": 2}]
        self.assertEqual(Base.from_json_string(json_string), expected_data)

    def test_create(self):
        dictionary = {"id": 5, "width": 10, "height": 20, "x": 1, "y": 2}
        b = Base.create(**dictionary)
        self.assertEqual(b.id, 5)
        self.assertEqual(b.width, 10)
        self.assertEqual(b.height, 20)
        self.assertEqual(b.x, 1)
        self.assertEqual(b.y, 2)


if __name__ == "__main__":
    unittest.main()
