from django.urls import path

from . import views

app_name = 'chats'

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/<user_pk>/', views.get_messages, name='get_messages'),
    path('remove_message/<pk>/', views.remove_message, name='remove_message'),
]
