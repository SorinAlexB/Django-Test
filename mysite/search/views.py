from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db import connection
from . import views
from django.urls import path, reverse
from polls.models import Service
from django.template import loader  
from django.shortcuts import render
from polls.models import Question, Choice
from django.views import generic
from django.utils import timezone
import Levenshtein

def search_ex(request):
    #if request.method == "POST":
    correct_words = ['pelerinaj', 'manastirile', 'rupestre', 'grup', 'dezvoltare', 'personala', 'socio-emotionala', 'emotionala', 'sedinta', 'terapie', 'psihologica', 'clinica', 'individuala', 'cuplu', 'familie', 'culinara', 'coaching', 'nutritie']
    if 'searched' in request.POST:
        services = Service.objects.none()
        searched = str(request.POST['searched'])
        for word in searched.split(" "):
              if word not in ['de','la','cu','pentru','De', 'La', 'Cu', 'Pentru', 'in', 'In']:
                    wordd = word[:] 
                    newword = min(correct_words, key=lambda x: Levenshtein.distance(word, x))
                    wordlower = newword[0].lower() + newword[1:]
                    wordupper = newword[0].upper() + newword[1:]
                    services1 = Service.objects.filter(name__contains = wordlower)
                    services2 = Service.objects.filter(name__contains = wordupper)
                    services |= services1 
                    services |= services2
                    wordlower = wordd[0].lower() + wordd[1:]
                    wordupper = wordd[0].upper() + wordd[1:]
                    services1 = Service.objects.filter(name__contains = wordlower)
                    services2 = Service.objects.filter(name__contains = wordupper)
                    services |= services1 
                    services |= services2

        return render(request, 
                       'search/search-ex.html',
                        {'searched':searched,
                         'services':services}
                )
    else:
        return render(request, 
                    'search/search-ex.html',
                    {}
        )
         

