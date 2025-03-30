
import feedparser
import json
from datetime import datetime
import os

# تحميل روابط RSS من ملف خارجي
with open("feeds_config.json", "r") as f:
    feeds = json.load(f)

all_articles = []

for source, url in feeds.items():
    feed = feedparser.parse(url)
    for entry in feed.entries[:10]:  # نأخذ فقط آخر 10 أخبار من كل مصدر
        article = {
            "source": source,
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", ""),
            "summary": entry.get("summary", "")[:300]
        }
        all_articles.append(article)

# تأكد أن مجلد الإخراج موجود
os.makedirs("output", exist_ok=True)

# حفظ النتائج في ملف JSON
with open("output/f1_news.json", "w", encoding="utf-8") as out_file:
    json.dump(all_articles, out_file, indent=2, ensure_ascii=False)

print(f"✅ تم استخراج {len(all_articles)} خبر وحفظها في output/f1_news.json")
