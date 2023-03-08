from django.shortcuts import render
from PyDictionary import PyDictionary

def homeview(request):
    return render(request, 'dictionary/index.html')

def searchview(request):
    word = request.GET.get('search')

    dictionary = PyDictionary()

    meanings = dictionary.meaning(word)

    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)

    context = {
        'word': word,
        'meanings': meanings,
        'synonyms': synonyms,
        'antonoyms': antonyms
    }
    return render(request, 'dictionary/search.html', context)
    return render(request, 'dictionary/search.html')



