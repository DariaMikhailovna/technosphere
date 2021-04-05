from django.http import JsonResponse


def home_page(request):
    print('Home page')
    return JsonResponse({'status': 'ok'})
