import requests

# create list of your chosen pokemon ids
pokemon_ids = [2, 3, 4, 5, 6, 7]

# use a for loop to get the pokemon name and moves for each id
for id in range(6):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_ids[id])
    response = requests.get(url)
    pokemon = response.json()
    pokemon_name = pokemon['forms'][0]['name']
    #print(pokemon_name)

    moves = pokemon['moves']
    moves_list = []
    for move in moves:
        move_name = move['move']['name']
        moves_list.append(move_name)

# format the name and moves data - you can print to check the output
    pokedex = f"{pokemon_name}: \n {moves_list} \n"
    #print(pokedex)

# write pokedex (pokemon name and moves to file)
    with open('pokedex.txt', 'a') as text_file:
        text_file.write(pokedex)
