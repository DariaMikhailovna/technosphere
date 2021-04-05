from django.http import JsonResponse


def create_chat(request):
    return JsonResponse({'status': 'ok'})


def get_chat_by_id(request, chat_id):
    print('id:', chat_id)
    return JsonResponse({'status': 'ok'})


def get_all_chats(request):
    return JsonResponse({'status': 'ok'})
