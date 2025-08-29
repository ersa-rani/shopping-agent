import os
import chainlit as cl
import google.generativeai as genai
import requests
import time
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to fetch products from API
def fetch_products():
    url = "https://hackathon-apis.vercel.app/api/products"  # You can change this
    try:
        response = requests.get(url)
        print(f"API Response Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"API Response Data: {data}")
            return data
        else:
            print(f"API Error: {response.text}")
            return []
    except Exception as e:
        print(f"Error fetching products: {e}")
        return []

# Format product data for context
def format_products(products):
    if not products:
        return "No products available"
    
    formatted_products = []
    for p in products:
        try:
            # Handle different possible field names
            title = p.get('title') or p.get('name') or p.get('product_name') or 'Unknown Product'
            price = p.get('price') or p.get('cost') or 'Price not available'
            description = p.get('description') or p.get('desc') or 'No description available'
            
            formatted_products.append(f"{title} - Rs.{price} - {description}")
        except Exception as e:
            print(f"Error formatting product: {e}")
            continue
    
    return "\n".join(formatted_products) if formatted_products else "No products available"

# Chainlit logic
@cl.on_message
async def main(message: cl.Message):
    user_query = message.content
    
    # Show loading message
    await cl.Message(content="🔄 Fetching products and analyzing your request...").send()
    
    products = fetch_products()
    product_context = format_products(products)
    
    # If no products from API, use sample data for testing
    if product_context == "No products available":
        product_context = """
Sample Products Available:
1. Wireless Bluetooth Headphones - Rs.1,299 - High-quality sound with noise cancellation
2. Smart Fitness Watch - Rs.2,499 - Track your health and fitness goals
3. Portable Power Bank - Rs.899 - 10000mAh capacity for all your devices
4. Wireless Mouse - Rs.599 - Ergonomic design for comfortable use
5. USB-C Cable Set - Rs.299 - Fast charging and data transfer
6. Gaming Keyboard - Rs.1,899 - RGB backlight with mechanical switches
7. Webcam HD - Rs.1,199 - 1080p resolution for video calls
8. Wireless Earbuds - Rs.1,599 - True wireless with touch controls
"""

    prompt = f"""
You are a friendly and helpful shopping assistant for an online store. The user asked: "{user_query}"

Available products in our store:
{product_context}

Please:
1. If products are available, suggest relevant items based on the user's query
2. Mention prices and key features of recommended products
3. Be conversational and enthusiastic about helping them find what they need
4. If no products match their query, suggest alternatives or ask for more details
5. Always be helpful and provide shopping advice

Remember: You're a shopping assistant, so focus on helping them find and choose products!
"""

    try:
        response = model.generate_content(prompt)
        await cl.Message(content=response.text).send()
    except Exception as e:
        if "429" in str(e) or "quota" in str(e).lower():
            await cl.Message(content="⚠️ Rate limit reached. Please wait a moment and try again, or upgrade your Gemini API plan.").send()
        else:
            await cl.Message(content=f"Sorry, I encountered an error: {str(e)}").send()
