from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("home page")
    return render(request, 'index.html')
def pleaces(request):
    return render(request, 'index1.html')
def books(request):
    return render(request, 'index2.html')
def hotel(request):
    return render(request, 'index3.html')
def cinema(request):
    return render(request, 'index4.html')