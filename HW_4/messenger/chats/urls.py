from django.urls import path
from . import views


# return {'chats': [{'id': chat.id, 'url': f'/detail/{chat.id}'}]}

urlpatterns = [
    path('create/', views.create_chat, name='create_chat'),
    path('', views.get_all_chats, name='get_all_chats'),
    path('<int:chat_id>/', views.get_chat_by_id, name='get_chat_by_id'),
]
