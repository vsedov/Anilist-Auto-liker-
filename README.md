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