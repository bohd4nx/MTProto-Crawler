import configparser
import sys
from pathlib import Path


class Config:
    def __init__(self):
        self.parser = configparser.ConfigParser()
        self._load_config()
        self._setup_properties()
        self._validate_config()

    def _load_config(self) -> None:
        config_file = Path('config.ini')
        if not config_file.exists():
            self._exit("Configuration file 'config.ini' not found!")
        self.parser.read(config_file, encoding='utf-8-sig')

    def _setup_properties(self) -> None:
        self._setup_github()
        self._setup_telegram()
        self._setup_tracker()

    def _setup_github(self) -> None:
        self.GITHUB_TOKEN = self.parser.get('GITHUB', 'TOKEN', fallback='').strip()

    def _setup_telegram(self) -> None:
        self.BOT_TOKEN = self.parser.get('TELEGRAM', 'BOT_TOKEN', fallback='').strip()
        self.CHAT_ID = self.parser.get('TELEGRAM', 'CHAT_ID', fallback='').strip()

    def _setup_tracker(self) -> None:
        self.CHECK_INTERVAL = self.parser.getint('TRACKER', 'CHECK_INTERVAL', fallback=300)

    def _validate_config(self) -> None:
        validation_rules = {
            "GITHUB > TOKEN": lambda: not self.GITHUB_TOKEN,
            "TELEGRAM > BOT_TOKEN": lambda: not self.BOT_TOKEN,
            "TELEGRAM > CHAT_ID": lambda: not self.CHAT_ID
        }

        invalid_fields = [field for field, check in validation_rules.items() if check()]

        if invalid_fields:
            error_msg = f"Missing required configuration fields:\n{chr(10).join(f'- {field}' for field in invalid_fields)}"
            self._exit(error_msg)

    @staticmethod
    def _exit(message: str) -> None:
        print(f"Error: {message}")
        sys.exit(1)


config = Config()
