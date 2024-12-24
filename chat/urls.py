from django.urls import path , include
from . import views 
urlpatterns = [
     path('chat/<str:room_name>/', views.chat_room, name='chat'),
]