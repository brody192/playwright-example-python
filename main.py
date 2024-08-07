from fastapi import FastAPI, Response
from playwright.async_api import async_playwright
import os

app = FastAPI()

@app.get("/")
async def root():
    async with async_playwright() as p:
        # browser = await p.chromium.connect_over_cdp(os.environ['BROWSER_PLAYWRIGHT_ENDPOINT']) # Use this call when browserless v1 is in use
        browser = await p.chromium.connect(os.environ['BROWSER_PLAYWRIGHT_ENDPOINT']) # Use this call when browserless v2 is in use

        context = await browser.new_context()
        page = await context.new_page()

        await page.set_viewport_size({'width': 1920, 'height': 1080});

        await page.goto('https://example.com')
        screenshot_bytes = await page.screenshot()

        await browser.close()

        return Response(content=screenshot_bytes, media_type='image/png')