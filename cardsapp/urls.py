from django.urls import path
from cardsapp import views

app_name = 'cardsapp'

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('<str:deck>/cards/', views.DeckView.as_view(), name='cards'),
]