# 🛒 AI Shopping Assistant

An AI-powered shopping assistant built with **Chainlit** and **Google Gemini**, designed to help users find the right products from an online store.  
It fetches live product data from an API and provides smart recommendations in a conversational way.

## ✨ Features
- 🔗 **Fetches products** from a real API (`https://hackathon-apis.vercel.app/api/products`)
- 🤖 **Powered by Google Gemini** for intelligent responses
- 💬 **Conversational shopping assistant** built with Chainlit
- 🛍️ Suggests products with **prices & descriptions**
- 🧠 Handles cases where products are missing by using fallback sample data
- 🚀 Ready for customization with your own product APIs

## 🛠️ Tech Stack
- [Python](https://www.python.org/)
- [Chainlit](https://docs.chainlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Requests](https://docs.python-requests.org/)

## ⚙️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/<ersa-rani>/shopping-agent.git
   cd shopping-agent
Create a virtual environment & install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file and add your Gemini API key:

ini
Copy code
GEMINI_API_KEY=your_api_key_here
Run the Chainlit app:

bash
Copy code
chainlit run app.py -w
Open the provided local URL to chat with your AI shopping assistant.

📸 Demo
👉 <img width="1230" height="669" alt="image" src="https://github.com/user-attachments/assets/aea89f84-f9cb-4fd4-b25e-b1a1378a339c" />


🔮 Future Improvements
Integrate with real e-commerce APIs

Add product filtering (price range, categories, ratings)

Enable checkout flow integration
