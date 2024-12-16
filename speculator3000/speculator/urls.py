from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/5/
    path("<int:card_id>/", views.card, name="card"),
]