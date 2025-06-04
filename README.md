💰 BitSage – Your First AI-Powered Financial Sidekick! 🌟

Welcome to BitSage, a beginner-friendly, rule-based chatbot that helps users explore the world of cryptocurrency through simple AI decision-making. Whether you're a curious investor or just learning Python, this project shows how logic and data can combine to provide smart crypto insights.
🚀 What Is BitSage?

BitSage is a Python-powered chatbot that:

    Recommends profitable cryptocurrencies (based on price trends & market cap)

    Suggests sustainable options (based on energy use & project viability)

    Answers user queries like:

        "Which coin is trending?"

        "What's the most eco-friendly crypto?"

        "Which one is best for long-term gains?"

🛠️ Features

    💬 Conversational Interface (via Gradio)

    📊 Rule-Based Decisions (no complex ML)

    🌱 Sustainability-Aware

    📈 Profitability Logic

    🧠 Friendly tone & simple advice

    🖥️ Runs in the browser – no need for installations or APIs!

📦 Tech Stack
Tool	Purpose
Python	Core programming language
Gradio	User interface (browser-based)
Logic	If-else decision tree
🧠 How It Works

BitSage uses a simple logic engine to scan a predefined dataset of 3 major cryptos:

crypto_db = {
  "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3/10},
  "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6/10},
  "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8/10}
}

It answers based on:

    🔼 Trends: Coins with "price_trend": "rising"

    🌍 Sustainability: "energy_use": "low" + high sustainability score

    💸 Profitability: "price_trend": "rising" + "market_cap": "high"



▶️ How To Run

    Clone the repo
    https://github.com/margret255/Bitsage_advisor

cd crypto-chatbot

    Install dependencies

pip install gradio

    Run the chatbot

python bot.py

    Chat in your browser!
    Gradio will open a local link like http://127.0.0.1:7860/

