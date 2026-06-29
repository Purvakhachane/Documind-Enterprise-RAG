import json
import os
from typing import List, Optional
from datetime import datetime
from uuid import uuid4

class ConversationService:
    def __init__(self, storage_path: str = "./conversations"):
        self.storage_path = storage_path
        
        # Create storage directory if it doesn't exist
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
    
    def create_conversation(self) -> str:
        """Create a new conversation and return its ID"""
        conversation_id = str(uuid4())
        conv_file = os.path.join(self.storage_path, f"{conversation_id}.json")
        
        conversation = {
            "conversation_id": conversation_id,
            "created_at": datetime.now().isoformat(),
            "history": []
        }
        
        with open(conv_file, 'w') as f:
            json.dump(conversation, f, indent=2)
        
        return conversation_id
    
    def add_message(self, conversation_id: str, question: str, answer: str) -> bool:
        """Add a message to conversation history"""
        conv_file = os.path.join(self.storage_path, f"{conversation_id}.json")
        
        if not os.path.exists(conv_file):
            return False
        
        with open(conv_file, 'r') as f:
            conversation = json.load(f)
        
        conversation["history"].append({
            "question": question,
            "answer": answer,
            "timestamp": datetime.now().isoformat()
        })
        
        with open(conv_file, 'w') as f:
            json.dump(conversation, f, indent=2)
        
        return True
    
    def get_conversation(self, conversation_id: str) -> Optional[dict]:
        """Get conversation history by ID"""
        conv_file = os.path.join(self.storage_path, f"{conversation_id}.json")
        
        if not os.path.exists(conv_file):
            return None
        
        with open(conv_file, 'r') as f:
            return json.load(f)
    
    def list_conversations(self) -> List[str]:
        """List all conversation IDs"""
        conv_files = [f[:-5] for f in os.listdir(self.storage_path) if f.endswith('.json')]
        return conv_files
    
    def delete_conversation(self, conversation_id: str) -> bool:
        """Delete a conversation"""
        conv_file = os.path.join(self.storage_path, f"{conversation_id}.json")
        
        if not os.path.exists(conv_file):
            return False
        
        os.remove(conv_file)
        return True

    def get_conversation_summary(self, conversation_id: str) -> Optional[dict]:
        """Generate a lightweight summary for a conversation."""
        conversation = self.get_conversation(conversation_id)
        if not conversation:
            return None

        history = conversation.get("history", [])
        if not history:
            return {
                "conversation_id": conversation_id,
                "summary": "No messages yet.",
                "message_count": 0,
            }

        questions = [item.get("question", "") for item in history if item.get("question")]
        answers = [item.get("answer", "") for item in history if item.get("answer")]
        summary_text = " ".join(answers[-2:]) if len(answers) >= 2 else " ".join(answers)
        summary = summary_text.strip() or "Conversation captured successfully."

        return {
            "conversation_id": conversation_id,
            "summary": summary[:220] + ("..." if len(summary) > 220 else ""),
            "message_count": len(history),
            "last_question": questions[-1] if questions else None,
        }
