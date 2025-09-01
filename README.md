# Professional Exiftool Metadata Extractor by FsociteyF

## English

A powerful Python tool to extract image metadata using `exiftool`. Displays results in English and saves them to both English and partially Arabic translated text files.

### Features

-   Comprehensive metadata extraction.
-   English display, English and Arabic file output.
-   Command-line arguments for image path, output directory, and file prefix.
-   Error handling.
-   FsociteyF branding.

### Requirements

-   Python 3.x
-   `exiftool` (install via `sudo apt-get install libimage-exiftool-perl` on Debian/Ubuntu or `brew install exiftool` on macOS)
-   `Pillow` (optional: `pip install Pillow`)

### Usage

Run `python3.11 exif_extractor.py` and enter the image path when prompted. Alternatively, provide the path as an argument:

```bash
python3.11 exif_extractor.py <image_path> [-o <output_dir>] [-p <prefix>]
```

Example:

```bash
python3.11 exif_extractor.py my_photo.jpg -o output -p my_report
```

Output files: `<prefix>_en.txt` (English) and `<prefix>_ar.txt` (Arabic).

### FsociteyF Rights

Developed by FsociteyF. 
web : https://fsocitey.neocities.org/

### How to view Arabic file with `nano`

1.  Open Terminal.
2.  Navigate to file directory: `cd ft-tool`
3.  Open file: `nano metadata_ar.txt`
4.  Inside `nano`: Use arrow keys to navigate, `Ctrl + W` to search, `Ctrl + X` to exit (save with `Y` then `Enter`).

---


![وصف الصورة](images/logo.png)


---
# أداة استخراج بيانات تعريف الصور الاحترافية من FsociteyF

## العربية

أداة بايثون قوية لاستخراج بيانات تعريف الصور باستخدام `exiftool`. تعرض النتائج بالإنجليزية وتحفظها في ملفات نصية بالإنجليزية ونسخة مترجمة جزئيًا للعربية.

### الميزات

-   استخراج شامل لبيانات التعريف.
-   عرض بالإنجليزية، وإخراج ملفات بالإنجليزية والعربية.
-   دعم وسائط سطر الأوامر لمسار الصورة، دليل الإخراج، وبادئة الملف.
-   معالجة الأخطاء.
-   تحمل علامة FsociteyF التجارية وحقوقها.

### المتطلبات

-   Python 3.x
-   `exiftool` (تثبيت عبر `sudo apt-get install libimage-exiftool-perl` على Debian/Ubuntu أو `brew install exiftool` على macOS)
-   `Pillow` (اختياري: `pip install Pillow`)

### الاستخدام

شغل `python3.11 exif_extractor.py` وأدخل مسار الصورة عند المطالبة. بدلاً من ذلك، قدم المسار كوسيطة:

```bash
python3.11 exif_extractor.py <مسار_الصورة> [-o <دليل_الإخراج>] [-p <بادئة_الملف>]
```

مثال:

```bash
python3.11 exif_extractor.py my_photo.jpg -o output -p my_report
```

ملفات الإخراج: `<بادئة>_en.txt` (إنجليزية) و `<بادئة>_ar.txt` (عربية).

### حقوق FsociteyF

تم تطوير هذه الأداة بواسطة FsociteyF.
web : https://fsocitey.neocities.org/

### كيفية عرض الملف العربي باستخدام `nano`

1.  افتح الطرفية.
2.  انتقل إلى دليل الملف: `cd ft-tool`
3.  افتح الملف: `nano metadata_ar.txt`
4.  داخل `nano`: استخدم مفاتيح الأسهم للتنقل، `Ctrl + W` للبحث، `Ctrl + X` للخروج (احفظ بـ `Y` ثم `Enter`).


