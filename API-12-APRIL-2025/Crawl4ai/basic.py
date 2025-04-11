import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig()  # Default browser configuration
    run_config = CrawlerRunConfig()   # Default crawl run configuration
    async with AsyncWebCrawler(config=browser_config,verbose=True) as crawler:
            result = await crawler.arun(url="https://en.wikipedia.org/wiki/Large_language_model", config=run_config, bypass_cache=False)
            print(f"Extracted content: {result.markdown}")


if __name__ == "__main__":
    asyncio.run(main())