from django.db import models

# Create your models here.

# Extension class
class Extension(models.Model):
    extensionName = models.CharField(max_length=100)
    extensionReleaseDate = models.DateField()
    

# Card class
class Card(models.Model):
    cardName = models.CharField(max_length=100)
    cardRarity = models.CharField(max_length=50)
    cardExtension = models.ForeignKey(Extension, on_delete=models.CASCADE)
    cardIndex = models.IntegerField("Index in its series (ex 079/121)")
    cardImage = models.URLField("URL which leads to an image of this card")

    def __str__(self):
        return "{} {} {} from {} series".format(self.cardRarity, self.cardName, self.cardExtension.extensionName, self.cardIndex)
    




