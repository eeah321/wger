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

دامنه‌ی این نسخه **`gym.mofcious.ir`** است و در `prod.env` تنظیم شده. فقط مطمئن شو
رکورد A دامنه به IP سرور اشاره می‌کند. Caddy خودش گواهی HTTPS (Let's Encrypt) می‌گیرد
و پورت ۴۴۳ را می‌شنود.

اگر دامنه را عوض کردی، در `prod.env` این سه خط را به‌روز کن:

```ini
SITE_DOMAIN=gym.mofcious.ir
SITE_URL=https://gym.mofcious.ir
CSRF_TRUSTED_ORIGINS=https://gym.mofcious.ir
```

## ایمیل

تنظیمات SMTP در `prod.env` است و روی Gmail (`smtp.gmail.com:587`) تنظیم شده. فقط
`EMAIL_HOST_PASSWORD` را با **App Password** گوگل پر کن (از
https://myaccount.google.com/apppasswords — نیاز به فعال بودن تأیید مرحله‌ای دارد).
بدون آن، ایمیل ثبت‌نام و بازیابی رمز کار نمی‌کند.

## کارهای بعدی (عمداً انجام نشده)

- **ویدیوهای تمرین‌ها**: فعلاً وصل نشده‌اند. تصاویر هست، ویدیوها نه.

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
