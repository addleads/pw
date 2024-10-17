import streamlit as st
import asyncio
import random
from playwright.async_api import async_playwright

st.title("Pw com Streamlit")

# Lista de user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36"
]

async def run_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Executar em modo headless
        
        selected_user_agent = random.choice(user_agents)
        
        context = await browser.new_context(user_agent=selected_user_agent)
        page = await context.new_page()
        await page.goto("http://google.com")
        title = await page.title()
        await browser.close()
        return title

async def main():
    title = await run_playwright()
    st.write(f"O título da página é: {title}")

if __name__ == '__main__':
    asyncio.run(main())
