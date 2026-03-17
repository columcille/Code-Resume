import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
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
