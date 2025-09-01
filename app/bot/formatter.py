from datetime import datetime


def format_commit_message(update_info):
    commit = update_info['commit']
    stats = update_info['stats']
    layer_number = update_info['layer_number']

    author_name = commit['commit']['author']['name']
    author_url = commit.get('author', {}).get('html_url', '#')
    commit_url = commit['html_url']
    commit_message = commit['commit']['message']
    commit_date = commit['commit']['author']['date']
    short_sha = commit['sha'][:8]

    date_obj = datetime.fromisoformat(commit_date.replace('Z', '+00:00'))
    formatted_date = date_obj.strftime('%d.%m.%Y at %H:%M UTC')

    tl_file_url = "https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/SourceFiles/mtproto/scheme/api.tl"

    return f"""🚀 <b>MTProto Layer Update!</b>

👤 <a href='{author_url}'><b>{author_name}</b></a> • <a href='{tl_file_url}'>scheme/api.tl</a>
📎 <a href='{commit_url}'>{short_sha}</a> • {formatted_date}
💬 <b>Message:</b> {commit_message}

📊 <b>Changes:</b>
<pre>{{
  "api_scheme": {layer_number},
  "changes": {{
    "type": "git",
    "additions": {stats['additions']},
    "deletions": {stats['deletions']},
    "files_changed": {stats['files_changed']}
  }}
}}
</pre>

@MTProtoUpdates • <a href='https://github.com/bohd4nx/MTProto-Crawler'>View on GitHub</a>"""
