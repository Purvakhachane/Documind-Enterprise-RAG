from fastapi import APIRouter, HTTPException
from backend.services.conversation_service import ConversationService
from backend.models.response import ConversationResponse

router = APIRouter(prefix="/api/conversations", tags=["conversations"])
conversation_service = ConversationService()

@router.post("/create")
def create_conversation():
    """Create a new conversation"""
    try:
        conversation_id = conversation_service.create_conversation()
        return {"conversation_id": conversation_id, "message": "Conversation created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{conversation_id}")
def get_conversation(conversation_id: str):
    """Get conversation history by ID"""
    try:
        conversation = conversation_service.get_conversation(conversation_id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        return conversation
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def list_conversations():
    """List all conversations"""
    try:
        conversations = conversation_service.list_conversations()
        return {"conversations": conversations, "total_count": len(conversations)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{conversation_id}")
def delete_conversation(conversation_id: str):
    """Delete a conversation"""
    try:
        if not conversation_service.delete_conversation(conversation_id):
            raise HTTPException(status_code=404, detail="Conversation not found")
        return {"message": "Conversation deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{conversation_id}/summary")
def get_conversation_summary(conversation_id: str):
    """Return a concise summary for a conversation."""
    try:
        summary = conversation_service.get_conversation_summary(conversation_id)
        if not summary:
            raise HTTPException(status_code=404, detail="Conversation not found")
        return summary
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
