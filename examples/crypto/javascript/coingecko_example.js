/**
 * CoinGecko API Example - Get Cryptocurrency Prices
 * Documentation: https://www.coingecko.com/api/documentation
 * Works in both Node.js and Browser
 */

/**
 * Get current cryptocurrency price
 * @param {string} coinId - Cryptocurrency ID (e.g., 'bitcoin', 'ethereum')
 * @param {string} vsCurrency - Currency to compare against (e.g., 'usd', 'eur')
 * @returns {Promise<object>} Price data
 */
async function getCryptoPrice(coinId = 'bitcoin', vsCurrency = 'usd') {
    try {
        // Endpoint for coin data (no API key required for basic usage!)
        const url = `https://api.coingecko.com/api/v3/coins/${coinId}`;

        const params = new URLSearchParams({
            localization: 'false',
            tickers: 'false',
            community_data: 'false',
            developer_data: 'false'
        });

        const response = await fetch(`${url}?${params}`);

        if (!response.ok) {
            if (response.status === 404) {
                console.error(`❌ Cryptocurrency '${coinId}' not found!`);
                return null;
            }
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Extract useful market data
        const marketData = data.market_data;
        const priceInfo = {
            name: data.name,
            symbol: data.symbol.toUpperCase(),
            currentPrice: marketData.current_price[vsCurrency],
            marketCap: marketData.market_cap[vsCurrency],
            priceChange24h: marketData.price_change_percentage_24h,
            high24h: marketData.high_24h[vsCurrency],
            low24h: marketData.low_24h[vsCurrency],
            circulatingSupply: marketData.circulating_supply,
            totalSupply: marketData.total_supply,
            ath: marketData.ath[vsCurrency],  // All-time high
            athDate: marketData.ath_date[vsCurrency]
        };

        return priceInfo;

    } catch (error) {
        console.error('❌ Request failed:', error.message);
        return null;
    }
}

/**
 * Get currently trending cryptocurrencies
 * @returns {Promise<Array>} List of trending coins
 */
async function getTrendingCoins() {
    try {
        const response = await fetch('https://api.coingecko.com/api/v3/search/trending');

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data.coins.slice(0, 5).map(coin => ({
            name: coin.item.name,
            symbol: coin.item.symbol,
            marketCapRank: coin.item.market_cap_rank
        }));

    } catch (error) {
        console.error('❌ Request failed:', error.message);
        return null;
    }
}

// Example usage
(async () => {
    // Get Bitcoin price
    const btc = await getCryptoPrice('bitcoin');

    if (btc) {
        console.log(`\n₿ ${btc.name} (${btc.symbol})`);
        console.log(`💰 Current Price: $${btc.currentPrice.toLocaleString()}`);
        console.log(`📊 Market Cap: $${btc.marketCap.toLocaleString()}`);
        const changeEmoji = btc.priceChange24h > 0 ? "📈" : "📉";
        console.log(`${changeEmoji} 24h Change: ${btc.priceChange24h.toFixed(2)}%`);
        console.log(`📏 24h Range: $${btc.low24h.toLocaleString()} - $${btc.high24h.toLocaleString()}`);
        console.log(`🏆 All-Time High: $${btc.ath.toLocaleString()}`);
    }

    // Get Ethereum price
    console.log('\n' + '='.repeat(50));
    const eth = await getCryptoPrice('ethereum');
    if (eth) {
        console.log(`\nⓔ ${eth.name} (${eth.symbol})`);
        console.log(`💰 Current Price: $${eth.currentPrice.toLocaleString()}`);
    }

    // Get trending coins
    console.log('\n' + '='.repeat(50));
    console.log('\n🔥 Trending Cryptocurrencies:');
    const trending = await getTrendingCoins();
    if (trending) {
        trending.forEach((coin, i) => {
            console.log(`${i + 1}. ${coin.name} (${coin.symbol}) - Rank #${coin.marketCapRank}`);
        });
    }
})();

// For Node.js, export functions
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { getCryptoPrice, getTrendingCoins };
}
