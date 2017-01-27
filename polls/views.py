from django.shortcuts import render
from django.http import HttpResponse
from polls.models import SearchLog

def index(request):
    latest_search = SearchLog.was_published_recently()
    context = {
    						'latest_search': latest_search,
    						'text': "Please Make a research"
    					}
    return render(request, 'polls/index.html', context)

def search(request):   
    key_words = request.POST.get("key_words")
    location = request.POST.get("location")
    log = SearchLog(key_words_text=key_words, location_text=location)
    log.save()
    latest_search = SearchLog.was_published_recently()
    results = log.search()
    if results == 0:
    	text = "Sry, '" + location + "' not recognized"
    else:
    	text = "Your search for " + key_words + " in " + location 
    context = {
    						'results': results,
    						'latest_search': latest_search,
    						'text': text
    					}
    return render(request, 'polls/index.html', context)

def detail(request, search_id):
    latest_search = SearchLog.was_published_recently()
    log = SearchLog.objects.get(id=search_id)
    results = log.search()
    if results == 0:
    	text = "Sry, '" + log.location_text + "'' not recognized"
    else:
    	text = "Your search for " + log.key_words_text + " in " + log.location_text 
    context = {
    						'results': results,
    						'latest_search': latest_search,
    						'text': text
    					}
    return render(request, 'polls/index.html', context)


