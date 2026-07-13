import unittest

from backend.services.upload_service import UploadService


class UploadServiceTests(unittest.TestCase):
    def test_upload_service_placeholder_returns_queue_metadata(self):
        service = UploadService()
        result = service.upload("sample.pdf", b"%PDF-1.4", "application/pdf")

        self.assertEqual(result["status"], "queued")
        self.assertEqual(result["filename"], "sample.pdf")
        self.assertEqual(result["size_bytes"], 8)
        self.assertEqual(result["content_type"], "application/pdf")


if __name__ == "__main__":
    unittest.main()
