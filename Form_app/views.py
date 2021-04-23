from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')


def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'gender': request.POST['gender'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['comment']

        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')
