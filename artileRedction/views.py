from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template import loader

from .models import Article
# Create your views here.


def index(request):
    article_list = Article.objects.all()
    # template = loader.get_template('artileRedction/index.html')
    context = {
        'article_list': article_list
    }
    # output = ', '.join([a.article_text for a in latest_article_list])
    return render(request, 'index.html', context)


# def detail(request, article_id):
#     return HttpResponse("You're looking at article %s." % article_id)


# def results(request, article_id):
#     response = "You're looking at the results of article %s."
#     return HttpResponse(response % article_id)
