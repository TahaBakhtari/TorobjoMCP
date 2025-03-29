from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import time

load_dotenv()

# Create MCP instance
mcp = FastMCP("instagram_caption_extractor")

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

if __name__ == "__main__":
    mcp.run(transport="stdio")