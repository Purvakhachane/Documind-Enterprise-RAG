import unittest
from fastapi.testclient import TestClient

from backend.main import app


class ErrorHandlingTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_missing_route_returns_consistent_error_payload(self):
        response = self.client.get("/does-not-exist")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("message", data)


if __name__ == "__main__":
    unittest.main()
