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
