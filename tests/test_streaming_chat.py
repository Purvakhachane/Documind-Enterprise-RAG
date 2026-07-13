import unittest
from fastapi.testclient import TestClient

from backend.main import app


class StreamingChatTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_streaming_chat_endpoint_returns_streamed_response(self):
        response = self.client.post(
            "/api/chat/stream",
            json={"question": "Describe the project."},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/plain", response.headers["content-type"])
        self.assertIn("dummy", response.text.lower())


if __name__ == "__main__":
    unittest.main()
