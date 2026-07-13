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
        self.assertFalse(data["success"])
        self.assertIn("message", data)
        self.assertEqual(data["status_code"], 404)

    def test_cors_headers_are_present_for_allowed_origin(self):
        response = self.client.options(
            "/api/chat",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access-control-allow-origin", response.headers)
        self.assertEqual(response.headers["access-control-allow-origin"], "http://localhost:3000")

    def test_health_endpoint_still_works_with_logging_middleware(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")
        self.assertIn("X-Process-Time", response.headers)


if __name__ == "__main__":
    unittest.main()
