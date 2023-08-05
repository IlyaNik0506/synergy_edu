from django.shortcuts import render


def text(request):
    text = 'Hello, world!'

    context = {
        'text': text,
    }
    return render(request, 'main/text.html', context)


def page(request):
    return render(request, 'main/page.html')
# Create your views here.
