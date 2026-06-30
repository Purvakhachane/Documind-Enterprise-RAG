import unittest
from fastapi.testclient import TestClient

from backend.main import app


class StatusEndpointTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_status_endpoint_returns_summary(self):
        response = self.client.get("/api/status")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["service"], "DocuMind Enterprise RAG")
        self.assertIn("document_count", data)
        self.assertIn("conversation_count", data)
        self.assertEqual(data["status"], "ready")


if __name__ == "__main__":
    unittest.main()
