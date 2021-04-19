from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Chat


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        chat = Chat()
        chat.author_id = request.POST['user']
        chat.created_date = timezone.now()
        chat.save()
        return JsonResponse({'chat_id': chat.pk})
    else:
        raise Http404


def get_chat_by_id(request, chat_id):
    if request.method == "GET":
        chat = get_object_or_404(Chat, pk=chat_id)
        return JsonResponse({'author': chat.author.username, 'title': chat.title, 'created_date': chat.created_date})
    else:
        raise Http404


def get_all_chats(request):
    chats = Chat.objects.all()
    data = [{'author': chat.author.username, 'title': chat.title, 'created_date': chat.created_date} for chat in chats]
    return JsonResponse({'chats': data})

