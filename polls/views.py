from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  for x in [1, 2, 3]:
    print(x)

  return HttpResponse("Hello Django")