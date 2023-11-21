from django.shortcuts import render, redirect
from django.urls import reverse
import requests
import random


def stych(request):
    return render(request, 'stych.html')


def catalog(request):
    return render(request, 'catalog.html')


def poetry(request):
    link_poems = 'http://127.0.0.1:8000/api/poem/?format=json'
    link_authors = 'http://127.0.0.1:8000/api/author/?format=json'
    link_themes = 'http://127.0.0.1:8000/api/theme/?format=json'
    poems = requests.get(link_poems).json()
    authors = requests.get(link_authors).json()
    themes = requests.get(link_themes).json()
    random_poems_id = random.randint(1, (len(poems)))
    random_authors_id = random.randint(1, (len(authors)))
    random_themes_id = random.randint(1, (len(themes)))
    context = {'poems': poems,
               'authors': authors,
               'themes': themes,
               'random_poems_id': random_poems_id,
               'random_authors_id': random_authors_id,
               'random_themes_id': random_themes_id
               }
    if request.method == "POST":
        author_id = request.POST.get('author')
        theme_id = request.POST.get('theme')
        l_author_id = request.POST.get('list_author_id')
        l_theme_id = request.POST.get('list_theme_id')

        if author_id:
            author_poems =[]
            for i in poems:
                if i['author'] == int(author_id):
                    author_poems.append(i)
            return render(request, 'stych.html',{'authors': authors,"author_poems": author_poems,'author_id': author_id})

        if theme_id:
            theme_poems = []
            for i in poems:
                if i['theme'] == int(theme_id):
                    theme_poems.append(i)
            return render(request, 'stych.html',{'theme_poems': theme_poems,'authors': authors, 'theme_id': theme_id})

        if l_author_id:
            list_author_id = int(l_author_id)
            return render(request, 'catalog.html', {'poems':poems, 'list_author_id':list_author_id, 'autors' :authors})

        if l_theme_id:
            list_theme_id = int(l_theme_id)
            return render(request, 'catalog.html', {'poems':poems, 'list_theme_id':list_theme_id, 'themes' :themes,'authors': authors})



        else:
            return render(request, 'stych.html', context)
    return render(request, 'poetry.html', context)


def crambo(request, poem_id):
    link_poems = 'http://127.0.0.1:8000/api/poem/?format=json'
    link_authors = 'http://127.0.0.1:8000/api/author/?format=json'
    poems = requests.get(link_poems).json()
    authors = requests.get(link_authors).json()
    return render(request, 'crambo.html',{'poems': poems,'authors': authors, 'poem_id':poem_id})
