from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Card

# Create your views here.
def card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, "speculator/card.html", {"card": card})