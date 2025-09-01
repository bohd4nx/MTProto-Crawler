import logging
import re

import requests

from app.config import config

logger = logging.getLogger(__name__)


class GitHubTracker:
    def __init__(self):
        self.headers = {"Authorization": f"token {config.GITHUB_TOKEN}"}
        self.last_sha = None
        self.initialized = False
        logger.info("GitHubTracker initialized")

    def get_all_commits(self):
        params = {"path": "Telegram/SourceFiles/mtproto/scheme/api.tl"}
        response = requests.get(
            "https://api.github.com/repos/telegramdesktop/tdesktop/commits",
            params=params,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    @staticmethod
    def extract_layer_number(commit_message):
        match = re.search(r'layer\s+(\d+)', commit_message, re.IGNORECASE)
        return int(match.group(1)) if match else 0

    def get_commit_stats(self, commit_sha):
        url = f"https://api.github.com/repos/telegramdesktop/tdesktop/commits/{commit_sha}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        stats = data.get('stats', {})
        return {
            'additions': stats.get('additions', 0),
            'deletions': stats.get('deletions', 0),
            'total': stats.get('total', 0),
            'files_changed': len(data.get('files', []))
        }

    def check_for_updates(self):
        commits = self.get_all_commits()
        # logger.info(f"Retrieved {len(commits)} commits from GitHub")

        if not self.initialized:
            self.last_sha = commits[0]['sha']
            logger.info(f"Initial SHA set to {self.last_sha}")
            self.initialized = True
            return []

        new_commits = []
        for commit in commits:
            if commit['sha'] == self.last_sha:
                break
            new_commits.append(commit)

        if new_commits:
            self.last_sha = new_commits[0]['sha']
            logger.info(f"Found {len(new_commits)} new commits, latest SHA: {self.last_sha}")

            processed_commits = [{
                'commit': commit,
                'stats': self.get_commit_stats(commit['sha']),
                'layer_number': self.extract_layer_number(commit['commit']['message'])
            } for commit in reversed(new_commits)]

            return processed_commits

        logger.info("No new commits found")
        return []
