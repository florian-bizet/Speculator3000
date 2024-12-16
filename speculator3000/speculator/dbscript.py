from .models import Series, Extension, Card
from django.db import models
import datetime

s = Series(seriesName = "Wizards Series")
s.save()

e = s.extension_set.create(extensionName="Base Set", extensionReleaseDate=datetime.date(1999, 1, 9))

c = e.card_set.create(cardName="Charizard 4/102", cardRarity="Holo Rare", cardIndex=4, cardImage="https://pkmncards.com/wp-content/uploads/charizard-base-set-bs-4.jpg")
'''
class Card(models.Model):
    cardName = models.CharField(max_length=100)
    cardRarity = models.CharField(max_length=50)
    cardExtension = models.ForeignKey(Extension, on_delete=models.CASCADE)
    cardIndex = models.IntegerField("Index in its series (ex 079/121)")
    cardImage = models.URLField("URL which leads to an image of this card")
'''