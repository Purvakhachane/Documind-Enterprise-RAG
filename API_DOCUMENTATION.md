# DocuMind Enterprise RAG - API Documentation

## Overview
DocuMind Enterprise is a Retrieval-Augmented Generation (RAG) system built with FastAPI. It provides APIs for:
- **Chat & QA**: Ask questions and get answers from your documents
- **Document Management**: Upload, list, and manage documents
- **Conversation History**: Maintain and retrieve conversation histories

---

## Base URL
```
http://localhost:8000/api
```

---

## API Endpoints

### Health Check
```
GET /health
```
Returns the health status of the service.

**Response:**
```json
{
  "status": "healthy",
  "service": "DocuMind Enterprise RAG"
}
```

---

### Chat Endpoints

#### Create/Continue Conversation
```
POST /api/chat
```
Send a question and receive an answer from the RAG system.

**Request Body:**
```json
{
  "question": "What is the main topic of the document?",
  "conversation_id": "uuid-here-optional"
}
```

**Response:**
```json
{
  "answer": "The main topic is...",
  "source": "document_name.pdf",
  "page": 1,
  "confidence": 0.85,
  "conversation_id": "uuid-here",
  "timestamp": "2024-01-15T10:30:00"
}
```

---

### Document Management Endpoints

#### Upload Document
```
POST /api/documents/upload
```
Upload a new document to the system.

**Parameters:**
- `file` (FormData, required): The document file to upload

**Response:**
```json
{
  "document_id": "doc_1234567890",
  "document_name": "example.pdf",
  "document_type": "application/pdf",
  "uploaded_at": "2024-01-15T10:30:00",
  "file_size": 102400
}
```

#### List All Documents
```
GET /api/documents/list
```
Retrieve all uploaded documents.

**Response:**
```json
{
  "documents": [
    {
      "document_id": "doc_1234567890",
      "document_name": "example.pdf",
      "document_type": "application/pdf",
      "uploaded_at": "2024-01-15T10:30:00",
      "file_size": 102400
    }
  ],
  "total_count": 1
}
```

#### Get Document Details
```
GET /api/documents/{doc_id}
```
Get metadata for a specific document.

**Response:**
```json
{
  "document_id": "doc_1234567890",
  "document_name": "example.pdf",
  "document_type": "application/pdf",
  "uploaded_at": "2024-01-15T10:30:00",
  "file_size": 102400
}
```

#### Delete Document
```
DELETE /api/documents/{doc_id}
```
Delete a document from the system.

**Response:**
```json
{
  "message": "Document deleted successfully"
}
```

---

### Conversation Endpoints

#### Create New Conversation
```
POST /api/conversations/create
```
Start a new conversation thread.

**Response:**
```json
{
  "conversation_id": "uuid-here",
  "message": "Conversation created"
}
```

#### Get Conversation History
```
GET /api/conversations/{conversation_id}
```
Retrieve the complete history of a conversation.

**Response:**
```json
{
  "conversation_id": "uuid-here",
  "created_at": "2024-01-15T10:30:00",
  "history": [
    {
      "question": "What is the document about?",
      "answer": "The document discusses...",
      "timestamp": "2024-01-15T10:30:05"
    }
  ]
}
```

#### List All Conversations
```
GET /api/conversations/
```
Get a list of all conversation IDs.

**Response:**
```json
{
  "conversations": ["uuid-1", "uuid-2", "uuid-3"],
  "total_count": 3
}
```

#### Delete Conversation
```
DELETE /api/conversations/{conversation_id}
```
Delete a conversation and its history.

**Response:**
```json
{
  "message": "Conversation deleted successfully"
}
```

---

## Error Responses

All endpoints may return error responses in the following format:

```json
{
  "error": "Error Type",
  "detail": "Description of what went wrong",
  "status_code": 400
}
```

### Common Status Codes
- `200`: Success
- `400`: Bad Request
- `404`: Not Found
- `422`: Validation Error
- `500`: Internal Server Error

---

## Example Usage

### Example 1: Start a Conversation
```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Summarize the document"
  }'
```

### Example 2: Upload a Document
```bash
curl -X POST "http://localhost:8000/api/documents/upload" \
  -F "file=@path/to/document.pdf"
```

### Example 3: Get Conversation History
```bash
curl -X GET "http://localhost:8000/api/conversations/{conversation_id}"
```

---

## Running the Server

```bash
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Access the interactive API documentation at: `http://localhost:8000/docs`

---

## Features Added

✅ **Document Management** - Upload, list, and delete documents
✅ **Conversation History** - Track multi-turn conversations
✅ **Structured Responses** - Enhanced response models with metadata
✅ **Error Handling** - Global exception handlers and validation
✅ **API Documentation** - Interactive Swagger UI included

---

## Storage
- Documents are stored in: `./documents/`
- Conversations are stored in: `./conversations/`
