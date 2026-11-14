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


