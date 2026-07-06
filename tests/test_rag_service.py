import unittest

from backend.services.rag_service import RAGService, ask_question


class RAGServiceTests(unittest.TestCase):
    def test_ask_question_returns_placeholder_response(self):
        response = ask_question("What is this project about?")

        self.assertIsInstance(response, dict)
        self.assertIn("answer", response)
        self.assertIn("source", response)
        self.assertIn("page", response)
        self.assertEqual(response["page"], 1)
        self.assertTrue(response["answer"])

    def test_rag_service_instance_supports_placeholder_queries(self):
        service = RAGService()
        response = service.ask_question("Summarize the system")

        self.assertEqual(response["source"], "Sample.pdf")
        self.assertEqual(response["page"], 1)


if __name__ == "__main__":
    unittest.main()
