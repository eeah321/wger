# استقرار wger (نسخه‌ی شخصی‌سازی‌شده)

همه‌ی تنظیمات از قبل در این پوشه تنظیم شده‌اند. **فقط یک دستور لازم است.**

## پیش‌نیاز

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin git
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"    # بعد از آن یک بار خارج/وارد شو
```

## اجرا

```bash
git clone https://github.com/eeah321/wger-custom.git
cd wger-custom/deploy

# ۱) ساخت ایمیج اختصاصی (یک بار؛ چند دقیقه)
docker build -f ../extras/docker/production/Dockerfile -t eeah321/wger-server:custom ..

# ۲) بالا آوردن کل سیستم
docker compose up -d

# ۳) گوش دادن به لاگ‌ها
docker compose logs -f web
```

همین. دیتابیس، کش، celery، PowerSync و وب‌سرور خودکار بالا می‌آیند؛
مهاجرت‌ها و لود دیتابیس تمرین‌ها خودکار انجام می‌شود.

## ادمین اول

```bash
docker compose exec web ./manage.py createsuperuser
```

## تنها تنظیم اختیاری: دامنه

اگر دامنه‌ی خودت را داری، در `prod.env` فقط این سه خط را عوض کن:

```ini
SITE_DOMAIN=fit.example.com
SITE_URL=https://fit.example.com
CSRF_TRUSTED_ORIGINS=https://fit.example.com
```

و رکوردهای DNS دامنه را به IP سرور بزن. Caddy خودش گواهی HTTPS (Let's Encrypt)
می‌گیرد و پورت ۴۴۳ را می‌شنود.

اگر دامنه نداری، `SITE_DOMAIN` را روی آدرس IP سرور بگذار
(مثلاً `SITE_DOMAIN=192.168.1.10`) — آن‌وقت HTTPS کار نمی‌کند و فقط HTTP باز می‌شود؛
در این حالت بهتر است پورت 80 را مستقیم باز کنی.

## به‌روزرسانی

```bash
cd wger-custom && git pull origin custom/backend
cd deploy
docker build -f ../extras/docker/production/Dockerfile -t eeah321/wger-server:custom ..
docker compose up -d
docker compose exec web ./manage.py migrate --noinput
```

## نکات

- **ایمیج ثابت است** (`eeah321/wger-server:custom`)، پس سیستم خودکار آپدیت نمی‌شود.
- **هیچ داده‌ای از اینترنت لود نمی‌شود**: همه‌ی `SYNC_*` و `*_ON_STARTUP` روی False
  تنظیم شده‌اند و دیتابیس تمرین‌ها فقط از fixtureهای همین ریپو لود می‌شود.
- **دیتابیس مال تو می‌ماند**: در ولوم `postgres-data`؛ با ری‌استارت پاک نمی‌شود.
- **ریپو خصوصی است** چون `prod.env` حاوی کلیدها (`SECRET_KEY`، `JWT_PRIVATE_KEY`،
  `POSTGRES_PASSWORD`) است. آن را پابلیک نکن.

## عیب‌یابی

```bash
docker compose logs -f web        # لاگ برنامه
docker compose logs -f caddy      # لاگ وب‌سرور
docker compose ps                 # وضعیت سرویس‌ها
```
