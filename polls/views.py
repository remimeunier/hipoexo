from django.shortcuts import render
from django.http import HttpResponse
from polls.models import SearchLog
import math

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
    total_page = math.ceil(results.__len__()/6.0)
    context = {	
    						'id': log.id,
    						'results': results[:6],
    						'latest_search': latest_search,
    						'text': text,
    						'range_total_page': range(1, total_page + 1),
    						'page': 1,
    						'total_page': total_page
    					}
    return render(request, 'polls/index.html', context)

def detail(request, search_id, page):
    latest_search = SearchLog.was_published_recently()
    log = SearchLog.objects.get(id=search_id)
    results = log.search()
    if results == 0:
    	text = "Sry, '" + log.location_text + "'' not recognized"
    else:
    	text = "Your search for " + log.key_words_text + " in " + log.location_text 
    total_page = math.ceil(results.__len__()/6.0)
    cut = ((int(page)-1) * 6) 
    context = {
    						'id': log.id,
    						'results': results[cut:cut+6],
    						'latest_search': latest_search,
    						'text': text,
    						'page': int(page),
    						'range_total_page': range(1, total_page +1),
    						'total_page': total_page
    					}
    return render(request, 'polls/index.html', context)


