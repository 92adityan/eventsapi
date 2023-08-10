from rest_framework.routers import DefaultRouter
from .views import (EventCreateView, EventListView, 
                    BookingCreateView, BookingListView,
                    user_registration, user_login)
from django.urls import path




urlpatterns = [
    path('events/create/', EventCreateView.as_view()),
    path('events/all/', EventListView.as_view()),
    path('events/booking/create', BookingCreateView.as_view()),
    path('events/booking/all', BookingListView.as_view()),
    path('user/registration/', user_registration),
    path('user/login/', user_login),
]



