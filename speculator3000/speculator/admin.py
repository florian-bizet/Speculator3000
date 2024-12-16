from django.contrib import admin

# Register your models here.
from .models import Series, Extension, Card

admin.site.register(Series)
admin.site.register(Extension)
admin.site.register(Card)