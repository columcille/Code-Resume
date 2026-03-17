import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"Error: Pokémon '{pokemon_name}' not found.")
    elif response.status_code == 408:
        print("Error: Request timed out. Please try again later.")
    elif response.status_code == 418:
        print("Error: I'm a teapot. This server is not meant to handle this request.")
    elif response.status_code == 500:
        print("Error: Server error. Please try again later.")
    else:
        print(f"Error: Unable to retrieve data for Pokémon '{pokemon_name}'.")
        return None
    
def main():
    pokemon_name = "Pikachu"
    data = get_pokemon_data(pokemon_name)
    if data:
        print(f"Name: {data['name'].capitalize()}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print("Types:")
        for type_info in data['types']:
            print(f" - {type_info['type']['name'].capitalize()}")
    else:
        print(f"Could not retrieve data for {pokemon_name}")


if __name__ == "__main__":
    main()
