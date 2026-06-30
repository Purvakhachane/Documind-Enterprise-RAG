import unittest
from fastapi.testclient import TestClient

from backend.main import app


class ProfessionalApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root_endpoint_returns_professional_landing_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])
        self.assertIn("DocuMind Enterprise RAG", response.text)
        self.assertIn("Professional", response.text)

    def test_unknown_route_returns_structured_error(self):
        response = self.client.get("/does-not-exist")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("error", data)
        self.assertEqual(data["status_code"], 404)


if __name__ == "__main__":
    unittest.main()
