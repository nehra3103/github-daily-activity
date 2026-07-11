from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

# Use Indian Standard Time
today = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d")

knowledge = Path("knowledge")
knowledge.mkdir(exist_ok=True)

file = knowledge / f"{today}.md"

if not file.exists():
    file.write_text(f"""# Daily Knowledge

Date: {today}

Today's automation is working successfully! 🚀
""")

today_file = Path("TODAY.md")
today_file.write_text(file.read_text())
