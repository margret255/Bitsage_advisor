

import gradio as gr

# Crypto DB
crypto_db = {
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3/10},
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6/10},
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8/10}
}


def chatbot_response(user_query):
    query = user_query.lower()

    if "sustainable" in query or "eco" in query:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"💡 Invest in {coin}! 🌱 It's eco-friendly and has long-term potential!"

    elif "profitable" in query or "best for profit" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f"🚀 {coin} is trending up and has a strong market presence. A good pick for profitability!"
        return "Hmm, no coin perfectly fits that rule. Consider diversifying."

    elif "trending" in query or "going up" in query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These cryptos are currently trending up: {', '.join(trending)}"

    elif "long-term" in query:
        return "Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀"

    elif "bye" in query or "exit" in query:
        return "BitSage: Catch you later! Remember, crypto is risky—always do your own research! 🧠💸"

    else:
        return "🤖 BitSage: Hmm 🤔 I didn’t get that. Ask me about trends, sustainability, or profitability."

#  Gradio UI
iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="💰 BitSage - Your Crypto Advisor",
    description="Ask about crypto trends, sustainability, and profitability!",
    theme="default"
)

iface.launch()
