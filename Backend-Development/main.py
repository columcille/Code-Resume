import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    # response = requests.head(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        print("OK!")
        return response.json()  # Uncomment this line to return the actual data
        # return response.headers  # For demonstration, we return headers instead of JSON data
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

def get_pokemon_data_with_timeout(pokemon_name, timeout=5):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            print("OK!")
            return response.json()
        elif response.status_code == 404:
            print(f"Error: Pokémon '{pokemon_name}' not found.")
        elif response.status_code == 418:
            print("Error: I'm a teapot. This server is not meant to handle this request.")
        elif response.status_code == 500:
            print("Error: Server error. Please try again later.")
        else:
            print(f"Error: Unable to retrieve data for Pokémon '{pokemon_name}'.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None

def get_ability_data(ability_name):
    url = f"https://pokeapi.co/api/v2/ability/{ability_name.lower()}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("OK!")
            return response.json()
        elif response.status_code == 404:
            print(f"Error: Ability '{ability_name}' not found.")
        elif response.status_code == 418:
            print("Error: I'm a teapot. This server is not meant to handle this request.")
        elif response.status_code == 500:
            print("Error: Server error. Please try again later.")
        else:
            print(f"Error: Unable to retrieve data for ability '{ability_name}'.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None
    
def main():
    pokemon_name = "Pikachu"
    data = get_pokemon_data(pokemon_name)
    if data:
        # for item in data: # This will print all the items in the data dictionary
        #     # print(f"{item}: {data[item]}")

        # for key in data.keys(): # This will print all the keys in the data dictionary
        #     print(f"{key}")
            
        print(f"Name: {data['name']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print("Types:")
        for type_info in data['types']:
            print(f" - {type_info['type']['name']}")
    else:
        print(f"Could not retrieve data for {pokemon_name}")

    response = get_ability_data("frisk")
    if response:
        print(f"Ability Name: {response['name']}")
        print(f"Effect: {response['effect_entries'][2]['effect']}")
        print(f"length of pokemon with this ability: {len(response['pokemon'])}")
    else:
        print("Could not retrieve ability data.")


if __name__ == "__main__":
    main()
