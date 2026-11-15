# changing_repo — تایم‌لاین تغییرات اعمال‌شده روی ریپو

این فایل وقایع همه‌ی تغییراتی را که روی این ریپو (wger) اعمال می‌شود، به‌ترتیب زمانی
ثبت می‌کند. هر بار تغییری اعمال شد، یک ورودی جدید **در انتهای همین فایل** اضافه کن.
هدف: داشتن تاریخچه‌ی قابل‌مشاهده و قابل‌برگشت از شخصی‌سازی‌ها و فارسی‌سازی‌ها.

- **ریپو:** `/opt/data/wger`
- **شاخه‌ی اصلی شخصی‌سازی:** `custom/backend`
- **نسخه‌ی پایه:** wger `2.8.0-dev.5` (commit `be0b52c43`)
- **آخرین به‌روزرسانی این فایل:** ۲۰۲۶-۱۱-۱۳

---

## الگوی هر ورودی

```
## YYYY-MM-DD — عنوان کوتاه

- **دسته:** ...
- **فایل‌ها:** ...
- **چه شد:** ...
- **چرا:** ...
- **برگشت:** ... (مثلاً `git revert <commit>` یا تغییر معکوس)
```

---

## ۲۰۲۶-۱۱-۱۳ — غیرفعال‌کردن تغذیه، اندازه‌گیری، جوائز، سینک wger.de و کاربران مهمان

- **دسته:** غیرفعال‌کردن امکانات (بک‌اند)
- **فایل‌ها:**
  - `settings/settings_global.py`
  - `settings/local_dev.py`
  - `wger/urls.py`
  - `wger/core/templates/navigation.html`
  - `wger/core/templates/user/overview.html`
  - `wger/software/templates/features.html`
- **چه شد:**
  1. **تغذیه (nutrition):** مسیر `/nutrition/` و تمام سرویس‌های API آن
     (`ingredient`, `ingredientinfo`, `ingredient-sync`, `ingredientweightunit`,
     `nutritionplan`, `nutritionplaninfo`, `nutritiondiary`, `meal`, `mealitem`,
     `ingredient-image`) از `wger/urls.py` حذف شد؛ منوی «Nutrition» از
     `navigation.html` برداشته شد؛ بخش «Nutrition plans» از صفحه‌ی کاربر
     و لینک آن در `features.html` حذف شد.
  2. **اندازه‌گیری‌ها (measurements):** مسیر `/measurement/` و سرویس‌های
     `measurement` و `measurement-category` حذف شد؛ منوی «Measurements» برداشته شد.
     ⚠️ اپ `measurements` به‌خاطر وابستگی `core` و `weight` به آن (وزن بدن در
     همین اپ ذخیره می‌شود) در `INSTALLED_APPS` باقی ماند — فقط سطح کاربری‌اش حذف شد.
  3. **جوائز (trophies):** `TROPHIES_ENABLED = False`؛ مسیر `/trophies/` و
     سرویس‌های `trophy`، `user-trophy`، `user-statistics` حذف شد؛ منوی «Trophies»
     و آیتم ادمین آن برداشته شد.
  4. **سینک با wger.de:** در `local_dev.py` مقدار `SYNC_INGREDIENTS_CELERY=False`،
     `SYNC_EXERCISE_IMAGES_CELERY=False` و `DOWNLOAD_INGREDIENTS_FROM='None'`
     (قبلاً در local_dev فعال بودند).
  5. **کاربران مهمان:** `ALLOW_GUEST_USERS = False` در `settings_global.py`
     و `local_dev.py` (قبلاً True بود).
- **چرا:** طبق درخواست کاربر — این بخش‌ها در نسخه‌ی شخصی‌سازی‌شده نمی‌خواهند.
- **چیزی که دست‌نخورده ماند:** اپ‌ها و مدل‌ها و مهاجرت‌ها سر جایشان؛ گالری
  تصاویر (gallery) فعال ماند؛ وزن بدن فعال ماند.
- **تأیید:** `manage.py check` بدون خطا (فقط هشدار از قبل موجود درباره‌ی `node_modules`).
- **برگشت:** `git revert` روی کامیت مربوطه، یا اجرای معکوس تغییرات بالا.

---

## ۲۰۲۶-۱۱-۱۳ — انتشار روی گیت‌هاب (fork کاربر)

- **دسته:** زیرساخت / انتشار
- **فایل‌ها:** (بدون تغییر کد — فقط انتشار)
- **چه شد:**
  - از ریپوی اصلی `wger-project/wger` یک fork به نام **`eeah321/wger`** ساخته شد.
  - شاخه‌ی `custom/backend` (کامیت `286c3aa14`) به fork پوش شد:
    `https://github.com/eeah321/wger/tree/custom/backend`
- **چرا:** کاربر خواست پروژه را مستقیم روی گیت‌هاب خودش ویرایش کند.
- **نکته‌ی امنیتي:** توکن دسترسی گیت‌هاب در چت ارسال شد؛ برای دفعات بعد توکن را در
  متغیر محیطی یا فایل محلی نگه دار و در چت نفرست. توکن در `.git/config` ذخیره نشد
  (پوش با URL یک‌بارمصرف انجام شد).
- **برگشت:** حذف شاخه از fork: `git push https://github.com/eeah321/wger.git --delete custom/backend`

---

## ۲۰۲۶-۱۱-۱۴ — دیتابیس تمرین‌ها فقط از داده‌ی خود کاربر (بدون هیچ منبع آنلاینی)

- **دسته:** دیتابیس / تمرین‌ها
- **فایل‌ها:**
  - `wger/exercises/fixtures/exercise-base-data.json`
  - `wger/exercises/fixtures/translations.json`
  - `wger/exercises/fixtures/equipment.json`
  - `wger/exercises/fixtures/muscles.json`
  - `wger/exercises/fixtures/categories.json`
- **چه شد:**
  - دیتابیس تمرین‌ها از فایل `parsed_exercises_matched_v3.json` کاربر ساخته شد:
    **۳۷۳ تمرین** (۴۹۹ رکورد مچ‌شده، یکتا شده بر اساس `repo.id`)، هر کدام با
    **۲ ترجمه (فارسی + انگلیسی)** = ۷۴۶ ترجمه.
  - نام، توضیح و مراحل فارسی از داده‌ی mrgym؛ نام و توضیح انگلیسی از رکورد وگر.
  - دسته‌ها (۸)، عضله‌ها (۱۶) و تجهیزات (۲۳) فارسی شدند و شناسه‌ها حفظ شد.
    برای تجهیزاتی که در وگر معادل نداشت (دستگاه، اسمیت ماشین، توپ پزشکی، طناب و…)
    ۱۱ تجهیزات جدید با شناسه‌ی ۱۳ تا ۲۳ اضافه شد.
  - عضله‌هایی که معادل وگر نداشتند (hip flexors, rotator cuff, adductors, abductors،
    ankles, feet, groin, cardiovascular system) در لیست عضلات نیامدند.
- **چرا:** کاربر خواست دیتابیس تمرین‌ها فقط از داده‌ی خودش باشد و هیچ منبع آنلاینی
  (wger.de) استفاده نشود.
- **دست‌نخورده:** `exercise-base-data.json` از ۸۷۲ رکورد رسمی به ۳۷۳ رکورد کاهش یافت؛
  نسخه‌ی اصلی در تاریخچه‌ی گیت موجود است.
- **تأیید:** با یک دیتابیس sqlite موقت (`settings/tmpverify.py` که بعد حذف شد)
  `migrate` + `loaddata` اجرا شد: **۱۲۰۴ شیء از ۷ fixture بدون خطا** لود شد
  (۳۷۳ تمرین، ۷۴۶ ترجمه، ۸ دسته، ۱۶ عضله، ۲۳ تجهیزات).
- **نکته:** `wger bootstrap` هنگام استارت همین fixtureها را لود می‌کند، پس دیگر
  تمرین‌های پیش‌فرض وگر در دیتابیس نیستند. برای جلوگیری از داده‌ی آنلاین باید در
  `prod.env` مقدار `SYNC_EXERCISES_ON_STARTUP/DOWNLOAD_*_ON_STARTUP/LOAD_ONLINE_FIXTURES_ON_STARTUP=False`
  و `SYNC_*_CELERY=False` باشد.
- **برگشت:** `git revert` روی کامیت مربوطه.

---

## ۲۰۲۶-۱۱-۱۴ — ریپوی خصوصی + deployment خودکار (بدون تنظیم دستی)

- **دسته:** زیرساخت / استقرار
- **فایل‌ها:**
  - `deploy/docker-compose.yml` (جدید)
  - `deploy/prod.env` (جدید)
  - `deploy/Caddyfile` (جدید)
  - `deploy/powersync/{powersync.yaml,sync_rules.yaml}` (جدید)
  - `deploy/README.md` (جدید)
  - `.github/workflows/` (حذف شد)
- **چه شد:**
  - ریپوی خصوصی **`eeah321/wger-custom`** ساخته شد (یک fork پابلیک نمی‌تواند خصوصی شود).
  - پوشه‌ی `deploy/` با **همه‌ی تنظیمات از قبل تنظیم‌شده** به ریپو اضافه شد:
    compose اختصاصی (بدون `include` و بدون تعارض)، `prod.env` کامل (به‌همراه
    `SECRET_KEY`، `JWT_*` و `POSTGRES_PASSWORD` تولیدشده)، `Caddyfile` برای HTTPS خودکار،
    و تنظیمات PowerSync.
  - CI workflowهای بالادستی حذف شد (برای یک fork شخصی لازم نیست و توکن بدون دسترسی
    `workflow` نمی‌تواند آن‌ها را پوش کند).
- **چرا:** کاربر خواست هیچ مقداری را دستی تعیین نکند و با یک دستور اجرا کند؛ و داده‌ها
  خصوصی هستند.
- **تأیید:** شاخه‌ی `custom/backend` روی هر دو ریپو پوش شد؛ ریپوی خصوصی `private: True`
  تأیید شد و پوشه‌ی `deploy/` در آن دیده می‌شود.
- **برگشت:** حذف پوشه‌ی `deploy/` و `git revert` روی کامیت‌ها.

---

## ۲۰۲۶-۱۱-۱۵ — زبان پیش‌فرض فارسی + تصاویر و ویدیوهای هر تمرین

- **دسته:** تنظیمات / مدیا
- **فایل‌ها:**
  - `settings/settings_global.py` — `LANGUAGE_CODE='fa'` و `TIME_ZONE='Asia/Tehran'`
  - `wger/exercises/fixtures/exercise-images.json` (جدید، ۳۷۳ رکورد)
  - `wger/exercises/fixtures/exercise-videos.json` (جدید، ۳۷۳ رکورد)
  - `wger/tasks.py` — لود این دو fixture در `bootstrap`
  - `deploy/media/exercise-images/**` (۳۷۳ تصویر webp، ~۱۱ مگابایت)
  - `deploy/media/videos.json` (مانفست ۳۷۳ ویدیو)
  - `deploy/download-videos.py` (جدید)
  - `deploy/docker-compose.yml` — سرویس `media-init` + مانت bind برای `media`
  - `deploy/.gitignore` (جدید)
- **چه شد:**
  - زبان پیش‌فرض سیستم فارسی و منطقه‌ی زمانی تهران شد.
  - تصاویر تمرین‌ها از `mrgym.ir` دانلود و در پوشه‌ی `media/exercise-images/` ریپو شد
    و با رکوردهای `exercises.exerciseimage` به هر تمرین وصل شد (هر تمرین یک تصویر
    اصلی `is_main=true`).
  - ویدیوها در یک جدول جدا (`exercises.exercisevideo`) به هر تمرین وصل شد. خود
    فایل‌های ویدیو (مجموعاً ~۱.۵ گیگابایت) در ریپو نمی‌آیند؛ سرویس `media-init` در
    اولین استقرار آن‌ها را از `mrgym.ir` دانلود می‌کند (با `DOWNLOAD_VIDEOS=false`
    غیرفعال می‌شود و هر فایلِ موجود دوباره دانلود نمی‌شود).
  - `media` به‌جای ولوم نامی، مانت bind به `deploy/media` شد تا هم تصاویر ریپو و هم
    فایل‌های دانلودشده در دسترس wger باشند.
- **چرا:** کاربر خواست زبان پیش‌فرض فارسی شود و تصاویر/ویدیوهای هر حرکت در جدول جدا
  به حرکت متصل شوند.
- **تأیید:** لود fixtureها روی دیتابیس موقت: **۱۹۵۰ شیء از ۹ fixture بدون خطا**
  (۳۷۳ تمرین، ۷۴۶ ترجمه، ۳۷۳ تصویر، ۳۷۳ ویدیو) و `manage.py check` بدون خطا.
- **برگشت:** `git revert` روی کامیت مربوطه.

---

## ۲۰۲۶-۱۱-۱۵ — تمرکز بر پایه: حذف ویدیوها + ایمیل Gmail

- **دسته:** باز‌پشتی / ایمیل
- **فایل‌ها:**
  - `wger/exercises/fixtures/exercise-videos.json` (حذف شد)
  - `wger/tasks.py` (خط لود fixture ویدیو حذف شد)
  - `deploy/download-videos.py` (حذف شد)
  - `deploy/docker-compose.yml` (سرویس `media-init` حذف شد)
  - `deploy/.gitignore`
  - `deploy/prod.env`
  - `deploy/README.md`
- **چه شد:**
  - کار ویدیو کنار گذاشته شد (کاربر: «اتصال ویدیوها رو بیخیال شو»). فقط تصاویر
    باقی ماندند.
  - تنظیمات ایمیل واقعی روی Gmail SMTP (`smtp.gmail.com:587`، TLS) با آدرس
    `moficious@gmail.com` در `prod.env` تنظیم شد. `EMAIL_HOST_PASSWORD` خالی است و
    باید با App Password گوگل پر شود.
- **چرا:** کاربر خواست روی کار کردن پایه‌ی برنامه تمرکز کنیم و ویدیو برای بعد باشد.
- **برگشت:** `git revert` روی کامیت مربوطه.




