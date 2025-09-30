
# Week 1 Assignment: Cryptocurrency Advisor Chatbot
# Theme: "Your First AI-Powered Financial Sidekick!" 🌟

# --- Step 1: Design the Chatbot Personality ---
bot_name = "CryptoBuddy"
bot_tone = "Friendly"

print(f"👋 Hey! I’m {bot_name}, your AI-powered crypto sidekick!")
print("Ask me about crypto trends, profitability, sustainability, or comparisons.\n")

# --- Step 2: Predefined Crypto Dataset ---
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}  

# --- Step 3: Chatbot Logic & Rules ---
def compare_coins(coin1, coin2):
    """Compare two coins side by side"""
    if coin1 not in crypto_db or coin2 not in crypto_db:
        return "⚠️ One of the coins you asked about isn’t in my database."

    c1, c2 = crypto_db[coin1], crypto_db[coin2]
    return (
        f"🔍 Comparison: {coin1} vs {coin2}\n\n"
        f"{coin1}: Trend = {c1['price_trend']}, Market Cap = {c1['market_cap']}, "
        f"Energy Use = {c1['energy_use']}, Sustainability = {c1['sustainability_score']}\n"
        f"{coin2}: Trend = {c2['price_trend']}, Market Cap = {c2['market_cap']}, "
        f"Energy Use = {c2['energy_use']}, Sustainability = {c2['sustainability_score']}\n"
    )

def get_response(user_query):
    user_query = user_query.lower()

    # --- New Feature: Compare two coins ---
    if "compare" in user_query:
        words = user_query.split()
        coins = [word.capitalize() for word in words if word.capitalize() in crypto_db]
        if len(coins) >= 2:
            return compare_coins(coins[0], coins[1])
        else:
            return "🤔 Please specify two coins to compare. Example: 'Compare Bitcoin and Cardano'."

    # Sustainability query
    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend}! It's eco-friendly and has strong long-term potential!"
    
    # Trending / rising cryptos
    elif "trending" in user_query or "rising" in user_query:
        rising_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These cryptos are trending up: {', '.join(rising_coins)}."
    
    # Profitability rule
    elif "profitable" in user_query or "best investment" in user_query:
        candidates = [coin for coin, data in crypto_db.items() 
                      if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if candidates:
            return f"💰 Based on profitability, {candidates[0]} looks like your best bet!"
        else:
            return "🤔 No crypto matches the strict profitability rule right now."
    
    # General coin info
    elif "bitcoin" in user_query:
        return "💡 Bitcoin is rising with high market cap, but has very high energy use (not eco-friendly)."
    elif "ethereum" in user_query:
        return "💡 Ethereum is stable with high market cap and medium energy use. A solid long-term option."
    elif "cardano" in user_query:
        return "💡 Cardano is rising with low energy use and a high sustainability score. Very eco-friendly!"
    
    else:
        return "🤷 Sorry, I didn’t get that. Try asking about 'sustainable', 'trending', 'profitable', or 'compare'."

# --- Step 4: Run the Chatbot Loop ---
while True:
    user_query = input("Potential Invester: ")
    if user_query.lower() in ["exit", "quit", "bye"]:
        print(f"{bot_name}: 👋 Bye! Happy investing!")
        break
    response = get_response(user_query)
    print(f"{bot_name}: {response}")
