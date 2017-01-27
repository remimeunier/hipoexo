from django.db import models
import foursquare  

class SearchLog(models.Model):
    key_words_text = models.CharField(max_length=200)
    location_text = models.CharField(max_length=200)

    def __str__(self):
        return self.key_words_text + ' in ' + self.location_text

    @staticmethod
    def was_published_recently():
        return SearchLog.objects.all().order_by('-id')[:20]

    def search(self):
    	client = foursquare.Foursquare(client_id='V131V0IPODZOAI4DH0TXB0W1VF4R1QCAHASGHJI35D3KJLWK', client_secret='L5RZFRA1K2KPH33H12BFD3MECOJKEBIJSLP14KXYRYW3A5AF')
    	try: 
    		json = client.venues.search(params={'query': self.key_words_text, 'near': self.location_text})
    		mylist = [] 
	    	for item in json['venues']:
	    		name = item['name']
	    		count = item['stats']['checkinsCount']
	    		if 'formattedPhone' in item['contact']:
	    			phone = item['contact']['formattedPhone']
	    		else:
	    			phone = 'No phone number provided'
	    		mylist.append({'name': name, 'phone': phone, 'count':count})
    	except:
    		mylist=0
    		pass

    	
    	return mylist

  #  		if 'formattedPhone' in item['contact']:
#    			print (item['name'] + ' checkin count : ' + str(item['stats']['checkinsCount']) + str(item['contact']['formattedPhone']))
#    		else:
#    			print (item['name'] + ' checkin count : ' + str(item['stats']['checkinsCount']))

    		

