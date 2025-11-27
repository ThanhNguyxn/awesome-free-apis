"""
PokeAPI Example - Get Pokemon Data
Documentation: https://pokeapi.co/docs/v2
"""
import requests

def get_pokemon(name_or_id):
    """
    Fetch Pokemon data by name or ID
    
    Args:
        name_or_id: Pokemon name (e.g., 'pikachu') or ID (e.g., 25)
    
    Returns:
        dict: Pokemon data including name, types, abilities, stats
    """
    try:
        # Make API request (no auth required!)
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name_or_id}')
        response.raise_for_status()  # Raise error for bad status codes
        
        # Parse JSON response
        data = response.json()
        
        # Extract useful information
        pokemon_info = {
            'name': data['name'].capitalize(),
            'id': data['id'],
            'height': data['height'] / 10,  # Convert to meters
            'weight': data['weight'] / 10,  # Convert to kg
            'types': [t['type']['name'] for t in data['types']],
            'abilities': [a['ability']['name'] for a in data['abilities']],
            'base_stats': {stat['stat']['name']: stat['base_stat'] 
                           for stat in data['stats']}
        }
        
        return pokemon_info
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Pokemon '{name_or_id}' not found!")
        else:
            print(f"❌ HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

# Example usage
if __name__ == '__main__':
    # Get Pikachu's data
    pikachu = get_pokemon('pikachu')
    
    if pikachu:
        print(f"\n⚡ {pikachu['name']} (#{pikachu['id']})")
        print(f"📏 Height: {pikachu['height']}m")
        print(f"⚖️  Weight: {pikachu['weight']}kg")
        print(f"🏷️  Types: {', '.join(pikachu['types'])}")
        print(f"💪 Abilities: {', '.join(pikachu['abilities'])}")
        print(f"📊 Base Stats:")
        for stat, value in pikachu['base_stats'].items():
            print(f"   - {stat}: {value}")
    
    # Try with Pokemon ID
    print("\n" + "="*50)
    charizard = get_pokemon(6)  # Charizard's ID
    if charizard:
        print(f"\n🔥 {charizard['name']} (#{charizard['id']})")
        print(f"🏷️  Types: {', '.join(charizard['types'])}")
