from django.shortcuts import render


def text(request):
    text = 'Hello, world!'

    context = {
        'text': text,
    }
    return render(request, 'desk/desk.html', context)


def page(request):
    return render(request, 'desk/page.html')
# Create your views here.
