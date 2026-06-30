import unittest
from fastapi.testclient import TestClient

from backend.main import app


class ChatMetadataTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_chat_response_includes_professional_metadata(self):
        response = self.client.post(
            "/api/chat",
            json={"question": "Explain the system briefly."},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreaterEqual(data["confidence"], 0)
        self.assertIn("conversation_id", data)


if __name__ == "__main__":
    unittest.main()
