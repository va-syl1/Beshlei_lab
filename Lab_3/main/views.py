from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def main(request):
    return render(request, 'templates.html', {'parameter': "test"})

def health(request):
    response = {'date': 'test1', 'current_page': "test2", 'server_info': "test3", 'client_info': "test4"}
    return JsonResponse(response)

