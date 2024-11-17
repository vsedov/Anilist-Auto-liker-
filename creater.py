# setup_project.py

import os
import shutil
from pathlib import Path

PROJECT_STRUCTURE = {
    "anilist_bot": {
        "core": {
            "auth": {
                "managers": ["__init__.py", "auth_manager.py", "cookie_manager.py"],
                "__init__.py": "",
            },
            "feed": {
                "managers": ["__init__.py", "feed_manager.py", "like_manager.py"],
                "strategies": [
                    "__init__.py",
                    "base.py",
                    "fixed.py",
                    "adaptive.py",
                    "time_based.py",
                    "smart.py",
                ],
                "__init__.py": "",
            },
            "navigation": {
                "managers": [
                    "__init__.py",
                    "navigation_manager.py",
                    "scroll_manager.py",
                ],
                "__init__.py": "",
            },
            "__init__.py": "",
        },
        "utils": {
            "drivers": ["__init__.py", "chrome.py", "firefox.py"],
            "logging": ["__init__.py", "setup.py", "formatters.py"],
            "helpers": ["__init__.py", "retry.py", "async_utils.py", "time_utils.py"],
            "__init__.py": "",
        },
        "config": {
            "settings": ["__init__.py", "config_manager.py", "validators.py"],
            "defaults": ["__init__.py", "default_config.py"],
            "__init__.py": "",
            "example_config.yaml": "",
        },
        "models": {
            "data": ["__init__.py", "stats.py", "feed_data.py"],
            "enums": ["__init__.py", "activity_types.py", "strategies.py", "speeds.py"],
            "__init__.py": "",
        },
        "exceptions": {
            "__init__.py": "",
            "bot_exceptions.py": "",
            "auth_exceptions.py": "",
            "feed_exceptions.py": "",
        },
        "tests": {
            "unit": {
                "auth": ["__init__.py", "test_auth_manager.py"],
                "feed": ["__init__.py", "test_feed_manager.py"],
                "navigation": ["__init__.py", "test_navigation_manager.py"],
                "__init__.py": "",
            },
            "integration": {
                "__init__.py": "",
                "test_bot_cycle.py": "",
                "test_feed_switching.py": "",
            },
            "fixtures": {
                "__init__.py": "",
                "mock_data.py": "",
                "mock_driver.py": "",
            },
            "conftest.py": "",
            "__init__.py": "",
        },
        "scripts": {
            "__init__.py": "",
            "setup_env.py": "",
            "cleanup.py": "",
            "update_drivers.py": "",
        },
        "__init__.py": "",
        "__main__.py": "",
    },
    "docs": {
        "api": {},
        "guides": {},
        "examples": {},
        "README.md": "",
    },
    "logs": {},
    "data": {
        "cookies": {},
        "stats": {},
        "cache": {},
    },
    ".git": {},
    ".github": {
        "workflows": {
            "test.yml": "",
            "lint.yml": "",
            "release.yml": "",
        },
    },
    "requirements": {
        "base.txt": "",
        "dev.txt": "",
        "test.txt": "",
    },
    ".gitignore": "",
    "README.md": "",
    "setup.py": "",
    "pyproject.toml": "",
    "LICENSE": "",
}


def create_directory_structure(base_path: Path, structure: dict) -> None:
    """Recursively create directory structure."""
    for name, content in structure.items():
        current_path = base_path / name

        if isinstance(content, dict):
            current_path.mkdir(exist_ok=True)
            create_directory_structure(current_path, content)
        else:
            current_path.touch()


def create_gitignore():
    """Create .gitignore file with common Python ignores."""
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Project specific
logs/
data/cookies/
data/stats/
data/cache/
chrome-data/
*.log
config.yaml
*.pkl

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
"""
    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip())


def create_readme():
    """Create README.md with project information."""
    readme_content = """
# AniList Bot

Advanced automation bot for AniList with multiple liking strategies and intelligent feed management.

## Features

- Multiple liking strategies (Fixed, Adaptive, Time-based, Smart)
- Intelligent feed management
- Rate limiting protection
- Cookie-based authentication
- Detailed statistics tracking
- Comprehensive logging

## Installation

1. Clone the repository
2. Install requirements:
   ```bash
   pip install -r requirements/base.txt
   ```
3. Copy example_config.yaml to config.yaml and update settings
4. Run the bot:
   ```bash
   python -m anilist_bot
   ```

## Project Structure

- `anilist_bot/`: Main package
  - `core/`: Core functionality
  - `utils/`: Utility functions and helpers
  - `config/`: Configuration management
  - `models/`: Data models and enums
  - `exceptions/`: Custom exceptions
- `tests/`: Test suite
- `docs/`: Documentation
- `data/`: Data storage
- `logs/`: Log files

## Development

Install development requirements:
```bash
pip install -r requirements/dev.txt
```

Run tests:
```bash
pytest
```

## License

[MIT License](LICENSE)
"""
    with open("README.md", "w") as f:
        f.write(readme_content.strip())


def create_requirements():
    """Create requirements files."""
    base_requirements = """
selenium>=4.15.2
loguru>=0.7.2
pyyaml>=6.0.1
"""

    dev_requirements = """
-r base.txt
black>=23.11.0
isort>=5.12.0
flake8>=6.1.0
mypy>=1.7.0
"""

    test_requirements = """
-r base.txt
pytest>=7.4.3
pytest-asyncio>=0.21.1
pytest-cov>=4.1.0
"""

    with open("requirements/base.txt", "w") as f:
        f.write(base_requirements.strip())
    with open("requirements/dev.txt", "w") as f:
        f.write(dev_requirements.strip())
    with open("requirements/test.txt", "w") as f:
        f.write(test_requirements.strip())


def create_main():
    """Create __main__.py with entry point."""
    main_content = """
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
"""
    with open("anilist_bot/__main__.py", "w") as f:
        f.write(main_content.strip())


def main():
    """Create project structure and initial files."""
    try:
        # Create base directory
        project_path = Path.cwd()

        # Create directory structure
        create_directory_structure(project_path, PROJECT_STRUCTURE)

        # Create specific files
        create_gitignore()
        create_readme()
        create_requirements()
        create_main()

        print("Project structure created successfully!")
        print("\nNext steps:")
        print("1. Create and activate a virtual environment:")
        print("   python -m venv venv")
        print("   source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate")
        print("2. Install requirements:")
        print("   pip install -r requirements/dev.txt")
        print("3. Copy example_config.yaml to config.yaml and update settings")
        print("4. Run the bot:")
        print("   python -m anilist_bot")

    except Exception as e:
        print(f"Error creating project structure: {str(e)}")


if __name__ == "__main__":
    main()
