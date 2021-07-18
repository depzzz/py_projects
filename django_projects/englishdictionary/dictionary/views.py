from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request,'dictionary/index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)
    return render(request,'dictionary/word.html', {
        'search' : search,
        'meaning' : meaning,
        'synonym' : synonym,
        'antonym' : antonym
    })