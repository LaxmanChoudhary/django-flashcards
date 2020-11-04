from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
	name = models.CharField(max_length=128)
	description  = models.CharField(max_length=256, blank=True)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='decks')
	is_public = models.BooleanField(default=False)
	is_editable = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def flashcard_count(self):
		return self.cards.count()

class Flashcard(models.Model):
	question = models.CharField(max_length=256)
	answer = models.TextField()
	code = models.TextField(blank=True)

	# related_field, for reverse queries
	# < Deck_object >.cards.all()
	deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
	
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cards')

	def __str__(self):
		return self.question

