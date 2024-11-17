import asyncio
from loguru import logger
from anilist_bot.core.auth.managers.auth_manager import AuthenticationManager
from anilist_bot.utils.logging.setup import setup_logging
from anilist_bot.config.settings.config_manager import ConfigManager

async def main():
    try:
        setup_logging()
        config = ConfigManager.load_config()

        # Initialize and run bot
        from anilist_bot.core.feed.managers.feed_manager import FeedManager
        bot = FeedManager(config)
        await bot.run()

    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot crashed: {str(e)}", exc_info=True)
    finally:
        logger.info("Bot session ended")

if __name__ == "__main__":
    asyncio.run(main())