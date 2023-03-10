import asyncio

import os
from dotenv import load_dotenv, find_dotenv

from poke_env.player import Player, RandomPlayer
from poke_env import PlayerConfiguration, ShowdownServerConfiguration


def poke_types(bot_pokemon_types):

    types = { "NORMAL": False, "FIRE": False, "WATER": False, "ELECTRIC": False, "GRASS": False, "ICE": False, "FIGHTING": False, "POISON": False, "GROUND": False, "FLYING": False, "PSYCHIC": False, "BUG": False, "ROCK": False, "GHOST": False, "DRAGON": False, "DARK": False, "STEEL": False }


    if "NORMAL" in str(bot_pokemon_types[0]) or "NORMAL" in str(bot_pokemon_types[1]):
        types["NORMAL"] = True
    if "FIRE" in str(bot_pokemon_types[0]) or "FIRE" in str(bot_pokemon_types[1]):
        types["FIRE"] = True
    if "WATER" in str(bot_pokemon_types[0]) or "WATER" in str(bot_pokemon_types[1]):
        types["WATER"] = True
    if "ELECTRIC" in str(bot_pokemon_types[0]) or "ELECTRIC" in str(bot_pokemon_types[1]):
        types["ELECTRIC"] = True
    if "GRASS" in str(bot_pokemon_types[0]) or "GRASS" in str(bot_pokemon_types[1]):
        types["GRASS"] = True
    if "ICE" in str(bot_pokemon_types[0]) or "ICE" in str(bot_pokemon_types[1]):
        types["ICE"] = True
    if "FIGHTING" in str(bot_pokemon_types[0]) or "FIGHTING" in str(bot_pokemon_types[1]):
        types["FIGHTING"] = True
    if "POISON" in str(bot_pokemon_types[0]) or "POISON" in str(bot_pokemon_types[1]):
        types["POISON"] = True
    if "GROUND" in str(bot_pokemon_types[0]) or "GROUND" in str(bot_pokemon_types[1]):
        types["GROUND"] = True
    if "FLYING" in str(bot_pokemon_types[0]) or "FLYING" in str(bot_pokemon_types[1]):
        types["FLYING"] = True
    if "PSYCHIC" in str(bot_pokemon_types[0]) or "PSYCHIC" in str(bot_pokemon_types[1]):
        types["PSYCHIC"] = True
    if "BUG" in str(bot_pokemon_types[0]) or "BUG" in str(bot_pokemon_types[1]):
        types["BUG"] = True
    if "ROCK" in str(bot_pokemon_types[0]) or "ROCK" in str(bot_pokemon_types[1]):
        types["ROCK"] = True
    if "GHOST" in str(bot_pokemon_types[0]) or "GHOST" in str(bot_pokemon_types[1]):
        types["GHOST"] = True
    if "DRAGON" in str(bot_pokemon_types[0]) or "DRAGON" in str(bot_pokemon_types[1]):
        types["DRAGON"] = True
    if "DARK" in str(bot_pokemon_types[0]) or "DARK" in str(bot_pokemon_types[1]):
        types["DARK"] = True
    if "STEEL" in str(bot_pokemon_types[0]) or "STEEL" in str(bot_pokemon_types[1]):
        types["STEEL"] = True


    return(types)

def poke_weak(types):
    
    weakness = { "NORMAL": 0, "FIRE": 0, "WATER": 0, "ELECTRIC": 0, "GRASS": 0, "ICE": 0, "FIGHTING": 0, "POISON": 0, "GROUND": 0, "FLYING": 0, "PSYCHIC": 0, "BUG": 0, "ROCK": 0, "GHOST": 0, "DRAGON": 0, "DARK": 0, "STEEL": 0 }
    
    if types["NORMAL"]:
        if types["FIGHTING"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = -1
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
        if types["FLYING"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = -1
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["WATER"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = -1
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = -1
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = -1
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
    if types["FIGHTING"]:
        if types["POISON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 4
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
        if types["ROCK"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 2
        if types["BUG"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 4
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
        if types["STEEL"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = -1
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 1/4
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 1/2
        if types["FIRE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 1/2
        if types["WATER"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 1/2
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 4
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/4
            weakness["STEEL"] = 0
    if types["FLYING"]:
        if types["POISON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/4
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["GROUND"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 0
            weakness["ICE"] = 4
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["ROCK"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 0
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = -1
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["BUG"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/4
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 4
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["GHOST"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["STEEL"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = -1
            weakness["GROUND"] = -1
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["FIRE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 4
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["WATER"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 4
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 4
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 2
            weakness["GROUND"] = -1
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/4
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["ICE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 4
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 4
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 2
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
    if types["POISON"]:
        if types["GROUND"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 0
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 1/4
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["BUG"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/4
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["GHOST"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/4
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["WATER"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
    if types["GROUND"]:
        if types["ROCK"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 4
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 4
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 1/4
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["BUG"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 0
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["GHOST"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/4
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["STEEL"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = -1
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/4
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["FIRE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 4
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["WATER"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 0
            weakness["ICE"] = 4
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["ELECTRIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["ICE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 4
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 2
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
    if types["ROCK"]:
        if types["BUG"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["STEEL"]:
            weakness["NORMAL"] = 1/4
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 4
            weakness["POISON"] = -1
            weakness["GROUND"] = 4
            weakness["FLYING"] = 1/4
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["FIRE"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/4
            weakness["WATER"] = 4
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 4
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["WATER"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/4
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 4
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["GRASS"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 2
        if types["DARK"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 4
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 2
    if types["BUG"]:
        if types["GHOST"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["STEEL"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 4
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = -1
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["FIRE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 4
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["WATER"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 4
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/4
            weakness["FLYING"] = 4
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["ELECTRIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
    if types["GHOST"]:
        if types["FIRE"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 1/2
        if types["WATER"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 1/2
        if types["ELECTRIC"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 1/2
        if types["ICE"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 2
        if types["DRAGON"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 2
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["DARK"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
    if types["STEEL"]:
        if types["FIRE"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 1/4
            weakness["FIGHTING"] = 2
            weakness["POISON"] = -1
            weakness["GROUND"] = 4
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/4
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/4
        if types["WATER"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 0
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/4
            weakness["FIGHTING"] = 2
            weakness["POISON"] = -1
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/4
        if types["ELECTRIC"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = -1
            weakness["GROUND"] = 4
            weakness["FLYING"] = 1/4
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/4
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = -1
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/4
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 2
            weakness["STEEL"] = 1/2
        if types["DRAGON"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 0
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = -1
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["DARK"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 4
            weakness["POISON"] = -1
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 1/2
    if types["FIRE"]:
        if types["ELECTRIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 4
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/4
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 1/2
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/4
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/4
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 1/2
    if types["WATER"]:
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 1/4
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["ELECTRIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/4
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 1/2
        if types["ICE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/4
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/4
            weakness["WATER"] = 1/4
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 1/2
    if types["GRASS"]:
        if types["ELECTRIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/4
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 4
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["ICE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 4
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 4
            weakness["ROCK"] = 0
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
    if types["ELECTRIC"]:
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 1/2
        if types["ICE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/4
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
    if types["PSYCHIC"]:
        if types["ICE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 2
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 2
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
    if types["ICE"]:
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] =0
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 2
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
    if types["DRAGON"]:
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0


    if not weakness["NORMAL"] and not weakness["FIRE"] and not weakness["WATER"] and  not weakness["ELECTRIC"] and  not weakness["GRASS"] and  not weakness["ICE"] and  not weakness["FIGHTING"] and  not weakness["POISON"] and  not weakness["GROUND"] and  not weakness["FLYING"] and  not weakness["PSYCHIC"] and  not weakness["BUG"] and  not weakness["ROCK"] and  not weakness["GHOST"] and  not weakness["DRAGON"] and  not weakness["DARK"] and  not weakness["STEEL"]:
        if types["NORMAL"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = -1
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["FIGHTING"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0
        if types["FLYING"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = -1
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["POISON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["GROUND"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = -1
            weakness["GRASS"] = 2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["ROCK"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["BUG"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["GHOST"]:
            weakness["NORMAL"] = -1
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = -1
            weakness["POISON"] = 1/2
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["STEEL"]:
            weakness["NORMAL"] = 1/2
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = -1
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 1/2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["FIRE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 2
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 1/2
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["WATER"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 2
            weakness["GRASS"] = 2
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["GRASS"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 2
            weakness["GROUND"] = 1/2
            weakness["FLYING"] = 2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["ELECTRIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 2
            weakness["FLYING"] = 1/2
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 1/2
        if types["PSYCHIC"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 1/2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 1/2
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 2
            weakness["STEEL"] = 0
        if types["ICE"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 2
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 1/2
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 2
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 0
            weakness["DARK"] = 0
            weakness["STEEL"] = 2
        if types["DRAGON"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 1/2
            weakness["WATER"] = 1/2
            weakness["ELECTRIC"] = 1/2
            weakness["GRASS"] = 1/2
            weakness["ICE"] = 2
            weakness["FIGHTING"] = 0
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = 0
            weakness["BUG"] = 0
            weakness["ROCK"] = 0
            weakness["GHOST"] = 0
            weakness["DRAGON"] = 1/2
            weakness["DARK"] = 0
            weakness["STEEL"] = 0
        if types["DARK"]:
            weakness["NORMAL"] = 0
            weakness["FIRE"] = 0
            weakness["WATER"] = 0
            weakness["ELECTRIC"] = 0
            weakness["GRASS"] = 0
            weakness["ICE"] = 0
            weakness["FIGHTING"] = 2
            weakness["POISON"] = 0
            weakness["GROUND"] = 0
            weakness["FLYING"] = 0
            weakness["PSYCHIC"] = -1
            weakness["BUG"] = 2
            weakness["ROCK"] = 0
            weakness["GHOST"] = 1/2
            weakness["DRAGON"] = 0
            weakness["DARK"] = 1/2
            weakness["STEEL"] = 0


    return(weakness)

def move_types(moves):

    move_types = { "NORMAL": False, "FIRE": False, "WATER": False, "ELECTRIC": False, "GRASS": False, "ICE": False, "FIGHTING": False, "POISON": False, "GROUND": False, "FLYING": False, "PSYCHIC": False, "BUG": False, "ROCK": False, "GHOST": False, "DRAGON": False, "DARK": False, "STEEL": False }


    for move in moves:
        if "NORMAL" in str(move.type):
            move_types["NORMAL"] = True
        if "FIRE" in str(move.type):
            move_types["FIRE"] = True
        if "WATER" in str(move.type):
            move_types["WATER"] = True
        if "ELECTRIC" in str(move.type):
            move_types["ELECTRIC"] = True
        if "GRASS" in str(move.type):
            move_types["GRASS"] = True
        if "ICE" in str(move.type):
            move_types["ICE"] = True
        if "FIGHTING" in str(move.type):
            move_types["FIGHTING"] = True
        if "POISON" in str(move.type):
            move_types["POISON"] = True
        if "GROUND" in str(move.type):
            move_types["GROUND"] = True
        if "FLYING" in str(move.type):
            move_types["FLYING"] = True
        if "PSYCHIC" in str(move.type):
            move_types["PSYCHIC"] = True
        if "BUG" in str(move.type):
            move_types["BUG"] = True
        if "ROCK" in str(move.type):
            move_types["ROCK"] = True
        if "GHOST" in str(move.type):
            move_types["GHOST"] = True
        if "DRAGON" in str(move.type):
            move_types["DRAGON"] = True
        if "DARK" in str(move.type):
            move_types["DARK"] = True
        if "STEEL" in str(move.type):
            move_types["STEEL"] = True


    return (move_types)

def hyper_effective(poke1, poke2):

    if poke1["NORMAL"] >= 4 and poke2["NORMAL"]:
        return True
    if poke1["FIRE"] >= 4 and poke2["FIRE"]:
        return True
    if poke1["WATER"] >= 4 and poke2["WATER"]:
        return True
    if poke1["ELECTRIC"] >= 4 and poke2["ELECTRIC"]:
        return True
    if poke1["GRASS"] >= 4 and poke2["GRASS"]:
        return True
    if poke1["ICE"] >= 4 and poke2["ICE"]:
        return True
    if poke1["FIGHTING"] >= 4 and poke2["FIGHTING"]:
        return True
    if poke1["POISON"] >= 4 and poke2["POISON"]:
        return True
    if poke1["GROUND"] >= 4 and poke2["GROUND"]:
        return True
    if poke1["FLYING"] >= 4 and poke2["FLYING"]:
        return True
    if poke1["PSYCHIC"] >= 4 and poke2["PSYCHIC"]:
        return True
    if poke1["BUG"] >= 4 and poke2["BUG"]:
        return True
    if poke1["ROCK"] >= 4 and poke2["ROCK"]:
        return True
    if poke1["GHOST"] >= 4 and poke2["GHOST"]:
        return True
    if poke1["DRAGON"] >= 4 and poke2["DRAGON"]:
        return True
    if poke1["DARK"] >= 4 and poke2["DARK"]:
        return True
    if poke1["STEEL"] >= 4 and poke2["STEEL"]:
        return True

    return False

def super_effective(poke1, poke2):

    if poke1["NORMAL"] >= 2 and poke2["NORMAL"]:
        return True
    if poke1["FIRE"] >= 2 and poke2["FIRE"]:
        return True
    if poke1["WATER"] >= 2 and poke2["WATER"]:
        return True
    if poke1["ELECTRIC"] >= 2 and poke2["ELECTRIC"]:
        return True
    if poke1["GRASS"] >= 2 and poke2["GRASS"]:
        return True
    if poke1["ICE"] >= 2 and poke2["ICE"]:
        return True
    if poke1["FIGHTING"] >= 2 and poke2["FIGHTING"]:
        return True
    if poke1["POISON"] >= 2 and poke2["POISON"]:
        return True
    if poke1["GROUND"] >= 2 and poke2["GROUND"]:
        return True
    if poke1["FLYING"] >= 2 and poke2["FLYING"]:
        return True
    if poke1["PSYCHIC"] >= 2 and poke2["PSYCHIC"]:
        return True
    if poke1["BUG"] >= 2 and poke2["BUG"]:
        return True
    if poke1["ROCK"] >= 2 and poke2["ROCK"]:
        return True
    if poke1["GHOST"] >= 2 and poke2["GHOST"]:
        return True
    if poke1["DRAGON"] >= 2 and poke2["DRAGON"]:
        return True
    if poke1["DARK"] >= 2 and poke2["DARK"]:
        return True
    if poke1["STEEL"] >= 2 and poke2["STEEL"]:
        return True

    return False

def out_speed(spe1, spe2):

    if spe1 > spe2:
        return True
    
    return False

def half_health(hp, health):

    if health <= 100:
        return True
    else:
        return False

def effective_move(weakness, moves):

    for move in moves:

        if weakness['NORMAL'] >= 4 and "NORMAL" in str(move.type):
            return move
        if weakness['FIRE'] >= 4 and "FIRE" in str(move.type):
            return move
        if weakness['WATER'] >= 4 and "WATER" in str(move.type):
            return move
        if weakness['ELECTRIC'] >= 4 and "ELECTRIC" in str(move.type):
            return move
        if weakness['GRASS'] >= 4 and "GRASS" in str(move.type):
            return move
        if weakness['ICE'] >= 4 and "ICE" in str(move.type):
            return move
        if weakness['FIGHTING'] >= 4 and "FIGHTING" in str(move.type):
            return move
        if weakness['POISON'] >= 4 and "POISON" in str(move.type):
            return move
        if weakness['GROUND'] >= 4 and "GROUND" in str(move.type):
            return move
        if weakness['FLYING'] >= 4 and "FLYING" in str(move.type):
            return move
        if weakness['PSYCHIC'] >= 4 and "PSYCHIC" in str(move.type):
            return move
        if weakness['BUG'] >= 4 and "BUG" in str(move.type):
            return move
        if weakness['ROCK'] >= 4 and "ROCK" in str(move.type):
            return move
        if weakness['GHOST'] >= 4 and "GHOST" in str(move.type):
            return move
        if weakness['DRAGON'] >= 4 and "DRAGON" in str(move.type):
            return move
        if weakness['DARK'] >= 4 and "DARK" in str(move.type):
            return move
        if weakness['STEEL'] >= 4 and "STEEL" in str(move.type):
            return move
        if weakness['NORMAL'] >= 2 and "NORMAL" in str(move.type):
            return move
        if weakness['FIRE'] >= 2 and "FIRE" in str(move.type):
            return move
        if weakness['WATER'] >= 2 and "WATER" in str(move.type):
            return move
        if weakness['ELECTRIC'] >= 2 and "ELECTRIC" in str(move.type):
            return move
        if weakness['GRASS'] >= 2 and "GRASS" in str(move.type):
            return move
        if weakness['ICE'] >= 2 and "ICE" in str(move.type):
            return move
        if weakness['FIGHTING'] >= 2 and "FIGHTING" in str(move.type):
            return move
        if weakness['POISON'] >= 2 and "POISON" in str(move.type):
            return move
        if weakness['GROUND'] >= 2 and "GROUND" in str(move.type):
            return move
        if weakness['FLYING'] >= 2 and "FLYING" in str(move.type):
            return move
        if weakness['PSYCHIC'] >= 2 and "PSYCHIC" in str(move.type):
            return move
        if weakness['BUG'] >= 2 and "BUG" in str(move.type):
            return move
        if weakness['ROCK'] >= 2 and "ROCK" in str(move.type):
            return move
        if weakness['GHOST'] >= 2 and "GHOST" in str(move.type):
            return move
        if weakness['DRAGON'] >= 2 and "DRAGON" in str(move.type):
            return move
        if weakness['DARK'] >= 2 and "DARK" in str(move.type):
            return move
        if weakness['STEEL'] >= 2 and "STEEL" in str(move.type):
            return move

    return max(moves, key=lambda move: move.base_power)

def max_dmg_move(moves):
    
    max_dmg = moves[0]

    for move in moves:
        if move.damage > 0 and move.base_power > max_dmg.base_power:
            max_dmg = move

    return max_dmg

def imune(weakness, moves):

    for move in moves:

        if weakness['NORMAL'] == -1 and "NORMAL" in str(move.type):
            moves.remove(move)
        if weakness['FIRE'] == -1 and "FIRE" in str(move.type):
            moves.remove(move)
        if weakness['WATER'] == -1 and "WATER" in str(move.type):
            moves.remove(move)
        if weakness['ELECTRIC'] == -1 and "ELECTRIC" in str(move.type):
            moves.remove(move)
        if weakness['GRASS'] == -1 and "GRASS" in str(move.type):
            moves.remove(move)
        if weakness['ICE'] == -1 and "ICE" in str(move.type):
            moves.remove(move)
        if weakness['FIGHTING'] == -1 and "FIGHTING" in str(move.type):
            moves.remove(move)
        if weakness['POISON'] == -1 and "POISON" in str(move.type):
            moves.remove(move)
        if weakness['GROUND'] == -1 and "GROUND" in str(move.type):
            moves.remove(move)
        if weakness['FLYING'] == -1 and "FLYING" in str(move.type):
            moves.remove(move)
        if weakness['PSYCHIC'] == -1 and "PSYCHIC" in str(move.type):
            moves.remove(move)

    return moves

def catch_em_all(my_poke, opo_poke, my_types, my_weakness, opo_types, opo_weakness, hyper_weak, super_weak, hyper_strong, super_strong, moves, switches):

    faster = out_speed(my_poke.base_stats['spe'], opo_poke.base_stats['spe'])
    half_health(my_poke.base_stats['hp'], my_poke.current_hp)
    moves = imune(opo_weakness, moves)
    print(moves)

    if hyper_weak and len(switches):
        print("Screw this!")
        return switches[0]
    
    if faster and hyper_strong:
        print("I'm faster and stronger!")
        return max_dmg_move(moves)

    if super_weak and not faster and len(switches):
        print("Perhaps next time!")
        return switches[0]

    if super_strong:
        print("I've got the upper hand!")
        return effective_move(opo_weakness, moves)

    print("Heads or tails?!")
    return max(moves, key=lambda move: move.base_power)


class MaxDamagePlayer(Player):
    def choose_move(self, battle):
        if battle.available_moves:


            bot_types = poke_types(battle.active_pokemon.types)
            bot_weakness = poke_weak(bot_types)
            bot_move_types = move_types(battle.available_moves)
            opo_types = poke_types(battle.opponent_active_pokemon.types)
            opo_weakness = poke_weak(opo_types)
            bot_hyper_weak = hyper_effective(bot_weakness, opo_types)
            bot_super_weak = super_effective(bot_weakness, opo_types)
            bot_hyper_strong = hyper_effective(opo_weakness, bot_move_types)
            bot_super_strong = super_effective(opo_weakness, bot_move_types)


            move = catch_em_all(battle.active_pokemon, battle.opponent_active_pokemon, bot_types, bot_weakness, opo_types, opo_weakness, bot_hyper_weak, bot_super_weak, bot_hyper_strong, bot_super_strong, battle.available_moves, battle.available_switches)

            return self.create_order(move)

            best_move = max(battle.available_moves, key=lambda move: move.base_power)
            return self.create_order(best_move)
        else:
            return self.choose_random_move(battle)


async def main():

    load_dotenv(find_dotenv())


    max_damage_player = MaxDamagePlayer(
        player_configuration=PlayerConfiguration(os.getenv("USER_NAME"), os.getenv("USER_PASSWD")),
        server_configuration=ShowdownServerConfiguration,
        battle_format="gen5randombattle",
    )


    await max_damage_player.send_challenges(os.getenv("OPPONENT"), n_challenges=1)

    await max_damage_player.accept_challenges(None, 1)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
