from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему этот магазин такой классный, и какой хорший товар.'
    }
    return render(request, 'main/about.html', context)
