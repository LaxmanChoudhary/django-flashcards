from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from cardsapp.models import Deck, Flashcard

# https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/#handling-forms-with-class-based-views
class HomeView(View):
	template_name = 'cardsapp/index.html'

	def get(self, request):
		decks = Deck.objects.all()
		ctx ={'decks': decks}
		return render(request, self.template_name, ctx)

class DeckView(ListView):
	paginate_by = 2
	context_object_name = 'cards'
	template_name = 'cardsapp/cardlist.html'

	def get_queryset(self):
		deck = Deck.objects.get(name=self.kwargs['deck'])
		return deck.cards.all()

	def get_context_data(self, **kwargs):
		args = super(ListView, self).get_context_data(**kwargs)
		args['deck'] = self.kwargs['deck']
		return args