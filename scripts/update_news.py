import feedparser
import json
import os

# Spectrum AI RSS Feed
RSS_URL = "https://spectrum.ieee.org/rss/artificial-intelligence"
NUM_ITEMS = 25  # Limit number of news items

# Parse RSS feed
feed = feedparser.parse(RSS_URL)

# Format news items
news_items = []
for entry in feed.entries[:NUM_ITEMS]:
    news_items.append({
        "title": entry.title,
        "link": entry.link,
        "pubDate": entry.published,
        "summary": entry.summary
    })

# Save to news.json
output_path = os.path.join("data", "news.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(news_items, f, indent=2, ensure_ascii=False)

print(f"Saved {len(news_items)} AI news items to {output_path}")
