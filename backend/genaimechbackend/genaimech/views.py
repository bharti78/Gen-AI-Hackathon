from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import get_response, post_response, post_chat, get_all_chat, new__chat, get__chat, get_prediction_percentage_asthma, get_prediction_percentage_cancer, get_prediction_percentage_cancer, get_prediction_percentage_diabetes, get_prediction_percentage_stroke, get_prescription
from .models import Chat, Message

from .util.auth import insert_signup, user_signin


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'Endpoint': '/', 'method': 'GET', 'body': None,
            'description': 'Returns an array of routes'},
        {'Endpoint': '/genaimech/', 'method': 'GET',
         'body': None, 'description': 'Returns an array of genaimech'},
        {'Endpoint': '/genaimech/', 'method': 'POST',
            'body': {'name': 'string', 'age': 'integer'}, 'description': 'Creates a new genaimech'},
        {'Endpoint': '/chat/<str:pk>/', 'method': 'POST',
            'body': {'message': 'string'}, 'description': 'Creates a new message in a chat'},
        {'Endpoint': '/chat/', 'method': 'GET',
            'body': None, 'description': 'Returns an array of chat'},
        {'Endpoint': '/chat/', 'method': 'POST',
            'body': {'chatName': 'string'}, 'description': 'Creates a new chat'},
        {'Endpoint': '/chat/<str:pk>/', 'method': 'GET',
            'body': None, 'description': 'Returns a chat with the given id'},
        {'Endpoint': '/form/<str:diagnosis>/', 'method': 'POST',
            'body': {'data': 'string'}, 'description': 'Returns the percentage of the diagnosis'},
        {'Endpoint': '/signup/', 'method': 'POST',
            'body': {'username': 'string', 'email': 'string', 'password': 'string'}, 'description': 'Creates a new user'},
        {'Endpoint': '/signin/', 'method': 'POST',
            'body': {'username': 'string', 'password': 'string'}, 'description': 'Signin a user'},
        {'Endpoint': '/prescription/', 'method': 'GET',
            'body': {'diseases': 'string'}, 'description': 'Returns a prescription for the diseases'}
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getGenaimech(request):
    if request.method == 'GET':
        return get_response('Get all genaimech')
    elif request.method == 'POST':
        return post_response('Create new genaimech')
    return get_response('Hello World')


@api_view(['POST'])
def chat(request, pk):
    print("Chat ID:", pk)
    message = request.data['message']
    
    # Handle "new" chat case
    if pk == "new":
        return Response({
            'message': 'Please create a new chat first before sending messages',
            'type': 'Error'
        }, status=400)
    
    try:
        # The frontend now sends numeric IDs directly, so we can use pk as is
        # Convert pk to integer for database lookup
        try:
            chat_id = int(pk)
        except ValueError:
            return Response({
                'message': 'Invalid chat ID format',
                'type': 'Error'
            }, status=400)
        
        # Get the chat by ID
        chat = Chat.objects.get(id=chat_id)
        
        # Save user message to database
        user_message = Message.objects.create(
            chat=chat,
            content=message,
            is_user_message=True
        )
        
        # Get AI response
        ai_response = post_chat(message)
        
        # Save AI response to database
        ai_message = Message.objects.create(
            chat=chat,
            content=ai_response.data['response'],
            is_user_message=False
        )
        
        # Return the AI response
        return ai_response
        
    except Chat.DoesNotExist:
        return Response({'message': 'Chat not found'}, status=404)
    except Exception as e:
        print("Error in chat view:", str(e))
        return Response({'message': str(e)}, status=500)


@api_view(['GET'])
def getallchats(request):
    try:
        print("Getting all chats...")
        response = get_all_chat()
        print("All chats response:", response.data)
        return response
    except Exception as e:
        print("Error in getallchats:", str(e))
        return Response({
            'message': str(e),
            'type': 'Error'
        }, status=500)


@api_view(['POST'])
def newchat(request):
    try:
        print("New chat request data:", request.data)
        chatName = request.data['chatName']
        print("Chat name:", chatName)
        return new__chat(chatName)
    except KeyError as e:
        print("Missing key in request:", e)
        return Response({
            'message': 'chatName is required',
            'type': 'Error'
        }, status=400)
    except Exception as e:
        print("Error in newchat view:", e)
        return Response({
            'message': str(e),
            'type': 'Error'
        }, status=500)


@api_view(['GET'])
def getchat(request, pk):
    try:
        # The frontend now sends numeric IDs directly, so we can use pk as is
        # Convert pk to integer for database lookup
        try:
            chat_id = int(pk)
        except ValueError:
            return Response({
                'message': 'Invalid chat ID format',
                'type': 'Error'
            }, status=400)
        
        return get__chat(chat_id)
    except Exception as e:
        print("Error in getchat view:", str(e))
        return Response({
            'message': str(e),
            'type': 'Error'
        }, status=500)


@api_view(['POST'])
def postForm(request, diagnosis):
    data = request.data['data']
    print("data", data)
    if diagnosis == 'asthma':
        return get_response(get_prediction_percentage_asthma(data))
    elif diagnosis == 'cancer':
        return get_response(get_prediction_percentage_cancer(data))
    elif diagnosis == 'diabetes':
        return get_response(get_prediction_percentage_diabetes(data))
    elif diagnosis == 'stroke':
        return get_response(get_prediction_percentage_stroke(data))
    else:
        return get_response('Invalid diagnosis')


@api_view(['POST'])
def signup(request):
    return insert_signup(request)


@api_view(['POST'])
def signin(request):
    return user_signin(request)


@api_view(['POST'])
def getPrescription(request):
    diseases = request.data['diseases']
    return get_prescription(diseases)
