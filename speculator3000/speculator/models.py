from django.db import models

# Create your models here.
# Card class
class Card(models.Model):
    cardName = models.CharField(max_length=100)
    cardRarity = models.CharField(max_length=50)
    cardSeries = models.CharField(max_length=100)
    cardIndex = models.IntegerField("Index in its series (ex 079/121)")
    cardImage = models.URLField("URL which leads to an image of this card")

    def __str__(self):
        return "{} {} {} from {} series".format(self.cardRarity, self.cardName, self.cardSeries, self.cardIndex)
    




