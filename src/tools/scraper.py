from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def scrape_brand_info(url: str):
    """
    Scrape website content to identify Brand Profile metrics.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        content = await page.content()
        await browser.close()
        
        soup = BeautifulSoup(content, 'html.parser')
        # Extract text for LLM processing
        text = " ".join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3'])])
        return text[:5000] # Limit content for LLM
