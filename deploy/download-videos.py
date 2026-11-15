#!/usr/bin/env python3
"""
دانلود خودکار ویدیوهای تمرین‌ها از mrgym.ir در اولین استقرار.

این اسکریپت در کانتینر `media-init` اجرا می‌شود و فایل‌ها را در
`media/exercise-video/...` می‌گذارد (همان پوشه‌ای که wger به‌عنوان
MEDIA_ROOT می‌شناسد). اگر فایلی از قبل هست دوباره دانلود نمی‌شود، پس
ری‌استارت بعدی سریع است. خطاها نادیده گرفته می‌شوند تا استقرار بلاک نشود.
"""
import json
import os
import sys
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(BASE, "media")
MANIFEST = os.path.join(MEDIA, "videos.json")


def main():
    if not os.path.exists(MANIFEST):
        print("no manifest, skipping")
        return 0

    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    print(f"{len(manifest)} videos to check")

    ok = skip = fail = 0
    for item in manifest:
        dest = os.path.join(MEDIA, item["path"])
        if os.path.exists(dest) and os.path.getsize(dest) > 1000:
            skip += 1
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        url = urllib.parse.quote(item["url"], safe=":/?=&%")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
                while True:
                    chunk = r.read(65536)
                    if not chunk:
                        break
                    f.write(chunk)
            ok += 1
            print(f"  ok {item['exercise']}: {os.path.getsize(dest)/1e6:.1f} MB")
        except Exception as e:  # noqa: BLE001 - best effort, never block deploy
            fail += 1
            print(f"  fail {item['exercise']}: {e}")
            if os.path.exists(dest):
                os.remove(dest)

    print(f"done: {ok} downloaded, {skip} already present, {fail} failed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
