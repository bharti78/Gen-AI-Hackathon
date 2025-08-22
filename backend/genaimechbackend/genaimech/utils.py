from rest_framework.response import Response
from .models import Chat, Message, User
# Temporarily disabled ML imports for database setup
# from .model.prediction import Model, get_predict_percentage_stroke, get_predict_percentage_diabetes, get_predict_percentage_cancer, get_predict_percentage_asthma
# from .llm.prescription import generate_prescription
# from .llm.prescription import chatbot


def get_response(data, status=200):
    return Response(data, status=status)


def post_response(data, status=201):
    return Response(data, status=status)


# Temporarily disabled model initialization for database setup
# model = Model()
# print("model", model)


def get_prediction_percentage_asthma(data_of_new_patient):
    # Temporarily disabled for database setup
    return {
        "type": "Success",
        "response": [[0.5, 0.5]]  # Dummy prediction
    }


def get_prediction_percentage_cancer(data_of_new_patient):
    # Temporarily disabled for database setup
    return {
        "type": "Success",
        "response": [[0.5, 0.5]]  # Dummy prediction
    }


def get_prediction_percentage_diabetes(data_of_new_patient):
    # Temporarily disabled for database setup
    return {
        "type": "Success",
        "response": [[0.5, 0.5]]  # Dummy prediction
    }


def get_prediction_percentage_stroke(data_of_new_patient):
    # Temporarily disabled for database setup
    return {
        "type": "Success",
        "response": [[0.5, 0.5]]  # Dummy prediction
    }


def post_chat(message, status=201):
    try:
        # Convert message to lowercase for easier matching
        user_message = message.lower().strip()
        
        # Enhanced medical doctor responses for ANY health issue
        if any(word in user_message for word in ['hello', 'hi', 'hey']):
            import random
            greetings = [
                "Hello! I'm Dr. AI. How can I help you today?",
                "Hi there! I'm Dr. AI, ready to assist with your health questions.",
                "Hey! Dr. AI here. What health concern can I help you with?",
                "Good day! I'm Dr. AI. How may I assist you today?"
            ]
            bot_response = random.choice(greetings)
        
        elif any(word in user_message for word in ['pain', 'hurt', 'ache', 'sore']):
            import random
            pain_responses = [
                "I understand you're experiencing pain. Please tell me:\n• Where is the pain located?\n• How long have you had it?\n• Rate your pain 1-10\n• What makes it better/worse?",
                "Pain can be concerning. Let me help assess this:\n• Location of the pain?\n• Duration and intensity (1-10 scale)?\n• What triggers or relieves it?\n• Any other symptoms?",
                "I'm here to help with your pain. Please describe:\n• Where exactly does it hurt?\n• How long has this been going on?\n• Pain level from 1-10?\n• What makes it worse or better?"
            ]
            bot_response = random.choice(pain_responses)
        
        elif any(word in user_message for word in ['fever', 'temperature', 'hot']):
            bot_response = "Fever assessment:\n• What's your temperature?\n• How long have you had it?\n• Any other symptoms?\n\n⚠️ Seek immediate care if: temp >103°F, severe headache, confusion"
        
        elif any(word in user_message for word in ['headache', 'head ache', 'migraine']):
            bot_response = "Headache assessment:\n• Location: front, back, sides?\n• Type: tension, migraine, sinus?\n• Duration and triggers?\n• Any nausea or light sensitivity?"
        
        elif any(word in user_message for word in ['cough', 'cold', 'flu', 'respiratory', 'breathing', 'chest']):
            bot_response = "Respiratory symptoms:\n• Cough type: dry/wet?\n• Duration and severity?\n• Any fever, body aches?\n• Shortness of breath?"
        
        elif any(word in user_message for word in ['stomach', 'nausea', 'vomiting', 'diarrhea', 'abdominal', 'digestive', 'gut']):
            bot_response = "GI symptoms:\n• What specific symptoms?\n• When did they start?\n• Any fever or abdominal pain?\n• Signs of dehydration?"
        
        elif any(word in user_message for word in ['tired', 'fatigue', 'weakness', 'exhausted', 'sleep']):
            bot_response = "Fatigue assessment:\n• How long have you felt this way?\n• Sleep quality changes?\n• Any other symptoms?\n• Recent stress or lifestyle changes?"
        
        elif any(word in user_message for word in ['medicine', 'medication', 'pill', 'drug', 'prescription']):
            bot_response = "Medication questions:\n• What specific medication?\n• What's your concern?\n• Are you currently taking it?\n• Any other medications?"
        
        elif any(word in user_message for word in ['emergency', 'urgent', 'severe', 'critical', 'dangerous']):
            bot_response = "🚨 MEDICAL EMERGENCY:\n\n📞 Call 911 or go to ER immediately!\n\nEmergency symptoms:\n- Chest pain\n- Severe breathing difficulty\n- Unconsciousness\n- Severe bleeding\n- Stroke signs (FAST)"
        
        elif any(word in user_message for word in ['thank', 'thanks', 'appreciate']):
            bot_response = "You're welcome! What else can I help you with today?"
        
        elif any(word in user_message for word in ['bye', 'goodbye', 'end', 'stop']):
            bot_response = "Take care! Stay healthy and feel free to return with any health questions. 👨‍⚕️"
        
        else:
            # Shorter response for general health issues
            import random
            general_responses = [
                f"Tell me more about '{message}':\n• What exactly are you experiencing?\n• When did it start?\n• How severe is it?\n• Any other symptoms?",
                f"I'd like to understand your '{message}' better:\n• Can you describe the symptoms?\n• When did this begin?\n• How much does it affect you?\n• Any related issues?",
                f"Let me help with '{message}':\n• What specific symptoms?\n• Timeline of onset?\n• Impact on daily life?\n• Other symptoms present?"
            ]
            bot_response = random.choice(general_responses)
        
        response = {
            'response': bot_response,
            'type': 'SUCCESS'
        }
        return Response(response, status=status)
    except Exception as e:
        return Response({'message': str(e)}, status=500)


def get_all_chat(status=200):
    try:
        # Get all chats from database
        chats = Chat.objects.all().order_by('-created_at')
        chat_list = []
        for chat in chats:
            chat_list.append({
                'id': chat.id,
                'name': chat.name,
                'created_at': chat.created_at,
                'user': chat.user.name if chat.user else 'No User'
            })
        
        response = {
            'type': 'Success',
            'response': chat_list
        }
        return Response(response, status=status)
    except Exception as e:
        return Response({'type': 'Error', 'message': str(e)}, status=status)


def new__chat(data, status=201):
    try:
        print("Creating chat with name:", data)
        
        # Validate data
        if not data or not isinstance(data, str) or len(data.strip()) == 0:
            return Response({
                'type': 'Error', 
                'message': 'Chat name is required and must be a non-empty string'
            }, status=400)
        
        # For now, create a chat without user association
        # In the future, you'll need to pass user_id
        chat = Chat.objects.create(name=data.strip())
        print("Chat created successfully with ID:", chat.id)
        
        response = {
            'type': 'Success',
            'response': {
                'id': chat.id,
                'chatName': chat.name,
                'created_at': chat.created_at
            }
        }
        return Response(response, status=status)
    except Exception as e:
        print("Error creating chat:", str(e))
        return Response({'type': 'Error', 'message': str(e)}, status=500)


def get__chat(pk, status=200):
    try:
        # Get chat by ID with messages
        chat = Chat.objects.get(id=pk)
        messages = chat.messages.all().order_by('created_at')
        
        message_list = []
        for msg in messages:
            message_list.append({
                'id': msg.id,
                'content': msg.content,
                'is_user_message': msg.is_user_message,
                'created_at': msg.created_at
            })
        
        data = {
            'type': 'Success',
            'response': {
                'chat': {
                    'id': chat.id,
                    'name': chat.name,
                    'created_at': chat.created_at,
                    'user': chat.user.name if chat.user else 'No User'
                },
                'messages': message_list
            }
        }
        return Response(data, status=status)
    except Chat.DoesNotExist:
        return Response({'type': 'Error', 'message': 'Chat not found'}, status=404)
    except Exception as e:
        return Response({'type': 'Error', 'message': str(e)}, status=500)


def get_prescription(diseases):
    print("diseases", diseases)
    # Temporarily disabled for database setup
    response = {
        'type': 'Success',
        'response': 'Prescription functionality temporarily disabled for database setup'
    }
    print("response", response)
    return Response(response, status=200)
