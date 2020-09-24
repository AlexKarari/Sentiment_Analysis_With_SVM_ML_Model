from django.db import models

# Create your models here.
class sentimentAnalyzer(models.Model):
    sentiment = models.CharField(max_length=1500)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "sentimentAnalyzers"
