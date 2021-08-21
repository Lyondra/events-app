from app import app
import unittest


class FlaskTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/results", content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_content(self):
        tester = app.test_client(self)
        response = tester.get("/results")
        self.assertEqual(response.content_type, "application/json")


if __name__ == '__main__':
    unittest.main()
