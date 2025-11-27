"""
CoinGecko API Example - Get Cryptocurrency Prices
Documentation: https://www.coingecko.com/api/documentation
"""
import requests

def get_crypto_price(coin_id='bitcoin', vs_currency='usd'):
    """
    Get current cryptocurrency price
    
    Args:
        coin_id: Cryptocurrency ID (e.g., 'bitcoin', 'ethereum', 'cardano')
        vs_currency: Currency to compare against (e.g., 'usd', 'eur', 'jpy')
    
    Returns:
        dict: Price data including current price, 24h change, market cap
    """
    try:
        # Endpoint for coin data (no API key required for basic usage!)
        url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
        
        params = {
            'localization': 'false',
            'tickers': 'false',
            'community_data': 'false',
            'developer_data': 'false'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract useful market data
        market_data = data['market_data']
        price_info = {
            'name': data['name'],
            'symbol': data['symbol'].upper(),
            'current_price': market_data['current_price'][vs_currency],
            'market_cap': market_data['market_cap'][vs_currency],
            'price_change_24h': market_data['price_change_percentage_24h'],
            '24h_high': market_data['high_24h'][vs_currency],
            '24h_low': market_data['low_24h'][vs_currency],
            'circulating_supply': market_data['circulating_supply'],
            'total_supply': market_data['total_supply'],
            'ath': market_data['ath'][vs_currency],  # All-time high
            'ath_date': market_data['ath_date'][vs_currency]
        }
        
        return price_info
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Cryptocurrency '{coin_id}' not found!")
        else:
            print(f"❌ HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

def get_trending_coins():
    """Get currently trending cryptocurrencies"""
    try:
        response = requests.get('https://api.coingecko.com/api/v3/search/trending')
        response.raise_for_status()
        
        data = response.json()
        trending = [
            {
                'name': coin['item']['name'],
                'symbol': coin['item']['symbol'],
                'market_cap_rank': coin['item']['market_cap_rank']
            }
            for coin in data['coins'][:5]  # Top 5
        ]
        return trending
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

# Example usage
if __name__ == '__main__':
    # Get Bitcoin price
    btc = get_crypto_price('bitcoin')
    
    if btc:
        print(f"\n₿ {btc['name']} ({btc['symbol']})")
        print(f"💰 Current Price: ${btc['current_price']:,.2f}")
        print(f"📊 Market Cap: ${btc['market_cap']:,.0f}")
        change_emoji = "📈" if btc['price_change_24h'] > 0 else "📉"
        print(f"{change_emoji} 24h Change: {btc['price_change_24h']:.2f}%")
        print(f"📏 24h Range: ${btc['24h_low']:,.2f} - ${btc['24h_high']:,.2f}")
        print(f"🏆 All-Time High: ${btc['ath']:,.2f}")
    
    # Get Ethereum price
    print("\n" + "="*50)
    eth = get_crypto_price('ethereum')
    if eth:
        print(f"\nⓔ {eth['name']} ({eth['symbol']})")
        print(f"💰 Current Price: ${eth['current_price']:,.2f}")
    
    # Get trending coins
    print("\n" + "="*50)
    print("\n🔥 Trending Cryptocurrencies:")
    trending = get_trending_coins()
    if trending:
        for i, coin in enumerate(trending, 1):
            print(f"{i}. {coin['name']} ({coin['symbol']}) - Rank #{coin['market_cap_rank']}")
