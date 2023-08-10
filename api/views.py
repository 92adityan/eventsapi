from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


class EventCreateView(CreateAPIView):
    '''
        ENDPOINT - /api/events/create
        only admin user can able to create events
    '''
    permission_classes = [permissions.IsAdminUser]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class BookingCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


@api_view(['POST'])
def user_registration(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response(
            {'error': 'Username and Password are required'}, 
            status = status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        password=password
    )

    user.save()

    return Response(
    {
        'message': 'user created successfully !',
    }, 
    status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
def user_login(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)