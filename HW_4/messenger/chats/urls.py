from django.urls import path
from . import views
from chats.view_set import NewChatViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', NewChatViewSet, basename='chats')
# router.register(r'<int:pk>', NewChatViewSet, basename='get_chat_by_id')
# router.register(r'create', NewChatViewSet, basename='create_chat')
# router.register(r'delete/<int:pk>', NewChatViewSet, basename='delete_chat')

urlpatterns = [
    # path('create/', views.create_chat, name='create_chat'),
    # path('delete/<int:chat_id>/', views.delete_chat, name='delete_chat'),
    # path('', views.get_all_chats, name='get_all_chats'),
    # path('<int:chat_id>/', views.get_chat_by_id, name='get_chat_by_id'),
    path('edit/<int:chat_id>/', views.chat_edit, name='chat_edit'),
]

urlpatterns += router.urls
