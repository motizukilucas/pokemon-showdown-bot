# Pokémon Showdown Bot
Based on [poke-env](https://github.com/hsahovic/poke-env)
Inpired by [Rempton Games](https://www.youtube.com/watch?v=C1KpQc9cWmM&t=314)

Thanks [Bulbagarden's list of type combinations](https://bulbapedia.bulbagarden.net/wiki/List_of_type_combinations_by_abundance) and [pokemondb's type chart](https://pokemondb.net/type) 

How to select always first move?

battle.team

    print(battle.active_pokemon.base_stats)
    # atk, def, hp, spa, spd, spe
    print(battle.active_pokemon.base_stats["spe"])
    print(battle.opponent_active_pokemon.base_stats["spe"])
    print(battle.active_pokemon.current_hp)
    print(battle.opponent_active_pokemon.current_hp)
    print(battle.active_pokemon.ability)
    print(battle.opponent_active_pokemon.ability)



## Running
You can run it locally with python3:

    pip3 install poke-env
    python3 bot.py

Or with docker:

    docker stop $(docker ps -aq) || true && docker rm $(docker ps -aq) || true && docker rmi $(docker images) || true && docker build . --no-cache -t pokemon-showdown-bot && docker run -d pokemon-showdown-bot

## TODO
- rule based bot
- train a ML algorytm to improve my bots AI
- dump poke-env lib and integrate with smogon's showdown myself
