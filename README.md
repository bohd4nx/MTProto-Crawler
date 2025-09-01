<div align="center">
  <h1>🚀 MTProto Layer Tracker</h1>
  <p>Real-time monitoring of Telegram Desktop MTProto API schema updates</p>
</div>

## 🚀 Features

- 🔍 **Real-time Monitoring** - Tracks changes to Telegram's MTProto API schema
- 📊 **Detailed Statistics** - Shows commit stats, layer numbers, and file changes
- ⚡ **Instant Notifications** - Beautiful formatted messages with commit details
- 📱 **Status Command** - Admin access to tracking statistics via `/start`

## 📋 Commands

| Command  | Description                 | Access     |
|----------|-----------------------------|------------|
| `/start` | View tracker status & stats | Admin only |

## 🛠️ Quick Setup

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/bohd4nx/MTProto-Crawler.git
   cd MTProto-Crawler
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Settings**
   ```ini
   # config.ini
   [GITHUB]
   TOKEN = your_github_token_here
   
   [TELEGRAM]
   BOT_TOKEN = your_bot_token_here
   CHAT_ID = your_chat_id_here
   ALLOWED_USERS = your_user_id_here
   
   [TRACKER]
   CHECK_INTERVAL = 300
   ```

4. **Launch Tracker**
   ```bash
   python main.py
   ```

## 📊 What Gets Tracked

- **File**: `Telegram/SourceFiles/mtproto/scheme/api.tl`
- **Repository**: [telegramdesktop/tdesktop](https://github.com/telegramdesktop/tdesktop)
- **Data**: Layer numbers, commit messages, file changes, statistics

## 🔧 Configuration

### GitHub Token

Create a personal access token at [GitHub Settings](https://github.com/settings/tokens) with repository read access.

### Telegram Setup

1. Create bot via [@BotFather](https://t.me/BotFather)
2. Get your chat ID from [@userinfobot](https://t.me/userinfobot)
3. Add your user ID to `ALLOWED_USERS` for `/start` access

---

<div align="center">
    <h4>Built with ❤️ by <a href="https://t.me/bohd4nx" target="_blank">Bohdan</a></h4>
</div>
