from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

load_dotenv()


mcp = FastMCP("combined_tools")


@mcp.tool()
async def search_torob(query: str, max_items: int = 10):
    """
    Search for products ( in Persian Lang ) on Torob and return price information.
    
    Args:
        query: The product name to search for
        max_items: Maximum number of items to return (default: 10)
        
    Returns:
        List of products with their title, price, and URL
    """
    url = f"https://api.torob.com/v4/base-product/search/?page=0&sort=popularity&size=24&query={query}&q={query}&source=next_desktop"
    
    data = []
    response = requests.get(url)
    results = response.json()["results"]
    
    for post in results:
        name = post["name1"]
        price = post["price"]
        product_url = "https://torob.com" + post["web_client_absolute_url"]

        if price != 0:
            data.append({"title": name, "price": price, "url": product_url})

            if len(data) >= max_items:
                return data
    
    next_page = response.json()["next"]
    while next_page and len(data) < max_items:
        response = requests.get(next_page)
        results = response.json()["results"]
        
        for post in results:
            name = post["name1"]
            price = post["price"]
            product_url = "https://torob.com" + post["web_client_absolute_url"]
            
            if price != 0:
                data.append({"title": name, "price": price, "url": product_url})

                if len(data) >= max_items:
                    return data
        
        next_page = response.json()["next"]
    
    return data

@mcp.tool()
async def get_instagram_caption(post_url: str):
    """
    Extracts caption from an Instagram post URL
    
    Args:
        post_url: The URL of the Instagram post
        
    Returns:
        The extracted caption or error message
    """
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    
    # Initialize ChromeDriver automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(post_url)
        time.sleep(5)
        
        selectors = [
            "//h1[contains(@class, '_ap3a') and contains(@class, '_aaco') and contains(@class, '_aacu')]",
            "//div[contains(@class, '_a9zr')]//h1",
            "//div[contains(@class, '_a9zs')]",
            "//div[contains(@class, '_aacl')]"
        ]
        
        for selector in selectors:
            caption_elements = driver.find_elements(By.XPATH, selector)
            if caption_elements:
                return caption_elements[0].text
        
        return "No caption found for this post."
            
    except Exception as e:
        return f"Error occurred: {str(e)}"
    finally:
        driver.quit()

@mcp.tool()
async def get_instagram_captiohelper(post_url: str):
    """
    Local helper function (not exposed as tool)
    Extracts product name from Instagram post caption by analyzing the caption text
    
    Args:
        post_url: The URL of the Instagram post
        
    Returns:
        The extracted product name or error message
    """
    try:

        caption = await get_instagram_caption(post_url)
        
        if caption.startswith("Error occurred:") or caption == "No caption found for this post.":
            return caption
        

        first_line = caption.split('\n')[0].strip()
        

        if '❤️' in first_line or '🔥' in first_line or '⭐' in first_line:
            parts = first_line.split('❤️') if '❤️' in first_line else \
                   first_line.split('🔥') if '🔥' in first_line else \
                   first_line.split('⭐')
            if len(parts) > 1:
                return parts[1].strip()

        if first_line.isupper():
            return first_line
        
        if '"' in first_line or "'" in first_line:
            quote_char = '"' if '"' in first_line else "'"
            parts = first_line.split(quote_char)
            if len(parts) > 1:
                return parts[1].strip()
        

        words = first_line.split()
        return ' '.join(words[:3]) if len(words) > 3 else first_line
        
    except Exception as e:
        return f"Error extracting product name: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")