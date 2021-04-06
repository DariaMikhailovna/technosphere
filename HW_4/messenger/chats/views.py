from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        return JsonResponse({'status': 'ok'})
    else:
        raise Http404


def get_chat_by_id(request, chat_id):
    if request.method == "GET":
        print('id:', chat_id)
        return JsonResponse({'status': 'ok'})
    else:
        raise Http404


def get_all_chats(request):
    if request.method == "GET":
        return JsonResponse({'status': 'ok'})
    else:
        raise Http404
