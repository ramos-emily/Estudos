from django.shortcuts import render

import random
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def character_name(request):
    categories = {
        "fantasy": ["Eldrin", "Thalindra", "Gorvok"],
        "futuristic": ["Xylo-7", "Nova", "Zentra"],
        "realistic": ["Emma", "Liam", "Sophia"],
    }
    category = request.query_params.get('category', 'fantasy')
    name = random.choice(categories.get(category, categories['fantasy']))
    return Response({"name": name})

@api_view(['GET'])
def story_idea(request):
    ideas = [
        "A hero must save a kingdom under siege by a dark sorcerer.",
        "A group of explorers discovers an ancient ruin filled with traps.",
        "An inventor's creation accidentally changes the course of history.",
    ]
    return Response({"story_idea": random.choice(ideas)})

@api_view(['GET'])
def rpg_scenario(request):
    scenarios = [
        "A bustling market where a mysterious trader offers a cursed item.",
        "A quiet forest with whispers of unseen watchers.",
        "A crumbling castle with hidden treasures and lurking dangers.",
    ]
    return Response({"scenario": random.choice(scenarios)})

@api_view(['GET'])
def phrase(request):
    phrases = [
        "Courage is not the absence of fear, but the triumph over it.",
        "Even the smallest person can change the course of history.",
        "The future belongs to those who believe in the beauty of their dreams.",
    ]
    return Response({"phrase": random.choice(phrases)})

