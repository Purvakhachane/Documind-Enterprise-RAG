import unittest
from fastapi.testclient import TestClient

from backend.main import app


class RequestValidationTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_invalid_chat_request_returns_validation_error(self):
        response = self.client.post(
            "/api/chat",
            json={"question": "a"},
        )
        self.assertEqual(response.status_code, 422)
        data = response.json()
        self.assertFalse(data["success"])
        self.assertIn("Validation failed", data["message"])


if __name__ == "__main__":
    unittest.main()
