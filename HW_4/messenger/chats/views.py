from django.http import JsonResponse, Http404, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Chat
from .forms import ChatForm


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        chat = Chat()
        chat.author_id = request.POST['user']
        chat.created_date = timezone.now()
        chat.save()
        return JsonResponse({'chat_id': chat.pk})
    else:
        return HttpResponseNotAllowed('POST')


def get_chat_by_id(request, chat_id):
    if request.method == "GET":
        chat = get_object_or_404(Chat, pk=chat_id)
        return JsonResponse({'author': chat.author.username, 'title': chat.title, 'created_date': chat.created_date, 'chat_id': chat_id})
    else:
        return HttpResponseNotAllowed('GET')


@csrf_exempt
def get_all_chats(request):
    if request.method == "GET":
        chats = Chat.objects.all()
        data = [{'author': chat.author.username, 'title': chat.title, 'created_date': chat.created_date, 'chat_id': chat.pk} for chat in chats]
        return JsonResponse({'chats': data})
    else:
        return HttpResponseNotAllowed('GET')


def delete_chat(request, chat_id):
    Chat.objects.filter(pk=chat_id).delete()
    return JsonResponse({'chat_id': 'deleted'})


def chat_edit(request, chat_id):
    if request.method == "POST":
        chat = get_object_or_404(Chat, pk=chat_id)
        form = ChatForm(request.POST, instance=chat)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.author = request.user
            chat.published_date = timezone.now()
            chat.save()
            return JsonResponse({'updated': chat_id})
        else:
            return HttpResponseBadRequest('Bad request')
    else:
        return HttpResponseNotAllowed('POST')
