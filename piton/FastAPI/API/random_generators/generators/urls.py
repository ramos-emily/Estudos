from django.urls import path
from .views import character_name, story_idea, rpg_scenario, phrase

urlpatterns = [
    path('character-name', character_name, name='character_name'),
    path('story-idea', story_idea, name='story_idea'),
    path('rpg-scenario', rpg_scenario, name='rpg_scenario'),
    path('phrase', phrase, name='phrase'),
]
