from django.db import models

class SearchLog(models.Model):
    key_words_text = models.CharField(max_length=200)
    location_text = models.CharField(max_length=200)

    def __str__(self):
        return self.key_words_text + ' in ' + self.location_text

    @staticmethod
    def was_published_recently():
        return SearchLog.objects.all().order_by('-id')[:20]
