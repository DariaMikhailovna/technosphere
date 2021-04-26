from django.urls import path
from . import views
from chats.view_set import ChatViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ChatViewSet, basename='chats')

urlpatterns = [
    path('create/', views.create_chat, name='create_chat'),
    path('delete/<int:chat_id>/', views.delete_chat, name='delete_chat'),
    # path('', views.get_all_chats, name='get_all_chats'),
    path('<int:chat_id>/', views.get_chat_by_id, name='get_chat_by_id'),
]

urlpatterns += router.urls
