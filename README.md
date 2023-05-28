# Pokémon Showdown Bot
Based on [poke-env](https://github.com/hsahovic/poke-env)
Inpired by [Rempton Games](https://www.youtube.com/watch?v=C1KpQc9cWmM&t=314)

Thanks [Bulbagarden's list of type combinations](https://bulbapedia.bulbagarden.net/wiki/List_of_type_combinations_by_abundance) and [pokemondb's type chart](https://pokemondb.net/type) 

## Poke-env Attributes

    battle.team
    print(battle.active_pokemon.base_stats)
    # atk, def, hp, spa, spd, spe
    print(battle.active_pokemon.base_stats["spe"])
    print(battle.opponent_active_pokemon.base_stats["spe"])
    print(battle.active_pokemon.current_hp)
    print(battle.opponent_active_pokemon.current_hp)
    print(battle.active_pokemon.ability)
    print(battle.opponent_active_pokemon.ability)

    return self.create_order(battle.available_switches[0])
> switches to first available pokemon

## TODO
- [x] If I'm hyper weak switch to next available pokemon
- [x] if outpseed and stronger use higest power attack
- [x] bug not switch if no available switch
- [x] bug avoid non damaging moves like roost if you want to attack
- [x] bug avoid imune moves like and eletric move against ground pokemon

## Running
You can run it locally with python3:

    pip3 install poke-env python-dotenv
    python3 ash.py

Or with docker:

    docker stop $(docker ps -aq) || true && docker rm $(docker ps -aq) || true && docker rmi $(docker images) || true && docker build . --no-cache -t pokemon-showdown-bot && docker run -d pokemon-showdown-bot

## Future Improvements
- Decision making based on bulbapedia data or other source 
- Refactor Ash
- Train a ML algorithm
- Try without include poke-env lib
