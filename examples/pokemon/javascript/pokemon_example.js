/**
 * PokeAPI Example - Get Pokemon Data
 * Documentation: https://pokeapi.co/docs/v2
 * Works in both Node.js and Browser
 */

/**
 * Fetch Pokemon data by name or ID
 * @param {string|number} nameOrId - Pokemon name (e.g., 'pikachu') or ID (e.g., 25)
 * @returns {Promise<object>} Pokemon data
 */
async function getPokemon(nameOrId) {
    try {
        // Make API request (no auth required!)
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${nameOrId}`);

        if (!response.ok) {
            if (response.status === 404) {
                console.error(`❌ Pokemon '${nameOrId}' not found!`);
                return null;
            }
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse JSON response
        const data = await response.json();

        // Extract useful information
        const pokemonInfo = {
            name: data.name.charAt(0).toUpperCase() + data.name.slice(1),
            id: data.id,
            height: data.height / 10,  // Convert to meters
            weight: data.weight / 10,  // Convert to kg
            types: data.types.map(t => t.type.name),
            abilities: data.abilities.map(a => a.ability.name),
            baseStats: Object.fromEntries(
                data.stats.map(stat => [stat.stat.name, stat.base_stat])
            )
        };

        return pokemonInfo;

    } catch (error) {
        console.error('❌ Request failed:', error.message);
        return null;
    }
}

// Example usage
(async () => {
    // Get Pikachu's data
    const pikachu = await getPokemon('pikachu');

    if (pikachu) {
        console.log(`\n⚡ ${pikachu.name} (#${pikachu.id})`);
        console.log(`📏 Height: ${pikachu.height}m`);
        console.log(`⚖️  Weight: ${pikachu.weight}kg`);
        console.log(`🏷️  Types: ${pikachu.types.join(', ')}`);
        console.log(`💪 Abilities: ${pikachu.abilities.join(', ')}`);
        console.log(`📊 Base Stats:`);
        for (const [stat, value] of Object.entries(pikachu.baseStats)) {
            console.log(`   - ${stat}: ${value}`);
        }
    }

    // Try with Pokemon ID
    console.log('\n' + '='.repeat(50));
    const charizard = await getPokemon(6);  // Charizard's ID
    if (charizard) {
        console.log(`\n🔥 ${charizard.name} (#${charizard.id})`);
        console.log(`🏷️  Types: ${charizard.types.join(', ')}`);
    }
})();

// For Node.js, you can also export the function
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { getPokemon };
}
