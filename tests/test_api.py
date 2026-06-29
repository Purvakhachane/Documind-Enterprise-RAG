import unittest
from fastapi.testclient import TestClient

from backend.main import app
from backend.routes.conversations import conversation_service


class DocuMindApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root_endpoint_returns_html_dashboard(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])
        self.assertIn("DocuMind Enterprise RAG", response.text)

    def test_chat_endpoint_returns_structured_response(self):
        response = self.client.post(
            "/api/chat",
            json={"question": "What is this system about?"},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("answer", data)
        self.assertIn("source", data)
        self.assertIn("confidence", data)
        self.assertIn("conversation_id", data)

    def test_conversation_summary_endpoint_returns_summary(self):
        conversation_id = conversation_service.create_conversation()
        conversation_service.add_message(conversation_id, "What is this project?", "It is an enterprise RAG app.")
        response = self.client.get(f"/api/conversations/{conversation_id}/summary")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("conversation_id", data)
        self.assertIn("summary", data)
        self.assertIn("message_count", data)


if __name__ == "__main__":
    unittest.main()
