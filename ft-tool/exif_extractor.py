
import subprocess
import json
import os
import argparse

translation_dict = {
    "FileName": "اسم الملف",
    "Directory": "المجلد",
    "FileSize": "حجم الملف",
    "FileType": "نوع الملف",
    "MIMEType": "نوع MIME",
    "ImageWidth": "عرض الصورة",
    "ImageHeight": "ارتفاع الصورة",
    "Make": "الشركة المصنعة",
    "Model": "الموديل",
    "DateTimeOriginal": "تاريخ ووقت الالتقاط الأصلي",
    "CreateDate": "تاريخ الإنشاء",
    "ModifyDate": "تاريخ التعديل",
    "Orientation": "الاتجاه",
    "XResolution": "دقة X",
    "YResolution": "دقة Y",
    "ResolutionUnit": "وحدة الدقة",
    "YCbCrPositioning": "تحديد موضع YCbCr",
    "ExifOffset": "إزاحة Exif",
    "GPSVersionID": "إصدار GPS",
    "GPSLatitudeRef": "مرجع خط العرض GPS",
    "GPSLatitude": "خط العرض GPS",
    "GPSLongitudeRef": "مرجع خط الطول GPS",
    "GPSLongitude": "خط الطول GPS",
    "GPSTimeStamp": "الطابع الزمني GPS",
    "GPSDateStamp": "الطابع الزمني لتاريخ GPS",
    "ColorSpace": "مساحة اللون",
    "ExifImageWidth": "عرض صورة Exif",
    "ExifImageHeight": "ارتفاع صورة Exif",
    "FocalLength": "البعد البؤري",
    "Flash": "الفلاش",
    "ExposureMode": "وضع التعرض",
    "WhiteBalance": "توازن اللون الأبيض",
    "DigitalZoomRatio": "نسبة التكبير الرقمي",
    "SceneCaptureType": "نوع التقاط المشهد",
    "GainControl": "التحكم في الكسب",
    "Contrast": "التباين",
    "Saturation": "التشبع",
    "Sharpness": "الحدة",
    "SubjectDistanceRange": "نطاق مسافة الهدف",
    "LensMake": "صانع العدسة",
    "LensModel": "موديل العدسة",
    "LensSpecification": "مواصفات العدسة",
    "LensSerialNumber": "الرقم التسلسلي للعدسة",
    "ShutterSpeedValue": "قيمة سرعة الغالق",
    "ApertureValue": "قيمة فتحة العدسة",
    "ExposureBiasValue": "قيمة تعويض التعرض",
    "MaxApertureValue": "أقصى قيمة لفتحة العدسة",
    "MeteringMode": "وضع القياس",
    "LightSource": "مصدر الضوء",
    "FNumber": "رقم F",
    "ExposureProgram": "برنامج التعرض",
    "ISOSpeedRatings": "تقييمات سرعة ISO",
    "DateTimeDigitized": "تاريخ ووقت الرقمنة",
    "SubSecTimeOriginal": "الوقت الأصلي بالمللي ثانية",
    "SubSecTimeDigitized": "الوقت الرقمي بالمللي ثانية",
    "FocalLengthIn35mmFormat": "البعد البؤري بتنسيق 35 مم",
    "SceneType": "نوع المشهد",
    "CustomRendered": "عرض مخصص",
    "InteroperabilityIndex": "فهرس التشغيل البيني",
    "InteroperabilityVersion": "إصدار التشغيل البيني",
    "ThumbnailOffset": "إزاحة الصورة المصغرة",
    "ThumbnailLength": "طول الصورة المصغرة",
    "UserComment": "تعليق المستخدم",
    "ComponentsConfiguration": "تكوين المكونات",
    "FlashpixVersion": "إصدار Flashpix",
    "ImageUniqueID": "معرف الصورة الفريد",
    "Compression": "الضغط",
    "PhotometricInterpretation": "التفسير الضوئي",
    "StripOffsets": "إزاحات الشريط",
    "RowsPerStrip": "صفوف لكل شريط",
    "StripByteCounts": "عدد بايتات الشريط",
    "XMPToolkit": "مجموعة أدوات XMP",
    "CreatorTool": "أداة الإنشاء",
    "MetadataDate": "تاريخ بيانات التعريف",
    "DocumentID": "معرف المستند",
    "InstanceID": "معرف المثيل",
    "OriginalDocumentID": "معرف المستند الأصلي",
    "Format": "التنسيق",
    "Description": "الوصف",
    "Subject": "الموضوع",
    "Keywords": "الكلمات المفتاحية",
    "Rating": "التقييم",
    "Rights": "الحقوق",
    "Creator": "المنشئ",
    "DateCreated": "تاريخ الإنشاء",
    "GPSAltitudeRef": "مرجع الارتفاع GPS",
    "GPSAltitude": "الارتفاع GPS",
    "GPSStatus": "حالة GPS",
    "GPSMeasureMode": "وضع قياس GPS",
    "GPSSpeedRef": "مرجع سرعة GPS",
    "GPSSpeed": "سرعة GPS",
    "GPSTrackRef": "مرجع مسار GPS",
    "GPSTrack": "مسار GPS",
    "GPSImgDirectionRef": "مرجع اتجاه صورة GPS",
    "GPSImgDirection": "اتجاه صورة GPS",
    "GPSMapDatum": "مرجع خريطة GPS",
    "GPSProcessingMethod": "طريقة معالجة GPS",
    "GPSAreaInformation": "معلومات منطقة GPS",
    "GPSDestLatitudeRef": "مرجع خط عرض الوجهة GPS",
    "GPSDestLatitude": "خط عرض الوجهة GPS",
    "GPSDestLongitudeRef": "مرجع خط طول الوجهة GPS",
    "GPSDestLongitude": "خط طول الوجهة GPS",
    "GPSDestBearingRef": "مرجع اتجاه الوجهة GPS",
    "GPSDestBearing": "اتجاه الوجهة GPS",
    "GPSDestDistanceRef": "مرجع مسافة الوجهة GPS",
    "GPSDestDistance": "مسافة الوجهة GPS",
    "GPSDifferential": "تفاضل GPS",
    "GPSHPositioningError": "خطأ تحديد المواقع الأفقي GPS",
    "SerialNumber": "الرقم التسلسلي",
    "FirmwareVersion": "إصدار البرنامج الثابت",
    "InternalSerialNumber": "الرقم التسلسلي الداخلي",
    "CameraTemperature": "درجة حرارة الكاميرا",
    "BatteryLevel": "مستوى البطارية",
    "ExposureTime": "وقت التعرض",
    "Aperture": "فتحة العدسة",
    "ISO": "ISO",
    "LensID": "معرف العدسة",
    "CircleOfConfusion": "دائرة التشويش",
    "FOV": "مجال الرؤية",
    "DOF": "عمق المجال",
    "HyperfocalDistance": "مسافة التركيز المفرط",
    "LightValue": "قيمة الضوء",
    "FlashCompensation": "تعويض الفلاش",
    "DigitalZoom": "التكبير الرقمي",
    "VibrationReduction": "تقليل الاهتزاز",
    "ActiveD-Lighting": "D-Lighting النشط",
    "PictureControl": "التحكم في الصورة",
    "ExposureDifference": "فرق التعرض",
    "LensType": "نوع العدسة",
    "Lens": "العدسة",
    "FocusMode": "وضع التركيز",
    "AFPoint": "نقطة التركيز التلقائي",
    "FocusPosition": "موضع التركيز",
    "ScalingFactor35efl": "عامل القياس 35efl",
    "SharpnessAppliedTo": "الحدة المطبقة على",
    "NoiseReduction": "تقليل الضوضاء",
    "ColorMode": "وضع اللون",
    "ToneMode": "وضع النغمة",
    "Lightness": "السطوع",
    "Shadows": "الظلال",
    "Highlights": "الإبرازات",
    "Contrast(2)": "التباين (2)",
    "Saturation(2)": "التشبع (2)",
    "Sharpness(2)": "الحدة (2)",
    "Hue": "درجة اللون",
    "FilterEffect": "تأثير الفلتر",
    "ExposureCompensation": "تعويض التعرض",
    "Date/TimeOriginal": "تاريخ/وقت الالتقاط الأصلي",
    "Create Date": "تاريخ الإنشاء",
    "Modify Date": "تاريخ التعديل",
    "GPS Latitude": "خط العرض GPS",
    "GPS Longitude": "خط الطول GPS",
    "GPS Altitude": "الارتفاع GPS",
    "Image Size": "حجم الصورة",
    "Megapixels": "ميغابكسل",
    "Focal Length": "البعد البؤري",
    "Lens Info": "معلومات العدسة",
    "Lens ID": "معرف العدسة",
    "Circle Of Confusion": "دائرة التشويش",
    "Field Of View": "مجال الرؤية",
    "Depth Of Field": "عمق المجال",
    "Hyperfocal Distance": "مسافة التركيز المفرط",
    "Light Value": "قيمة الضوء",
    "Flash Compensation": "تعويض الفلاش",
    "Digital Zoom": "التكبير الرقمي",
    "Vibration Reduction": "تقليل الاهتزاز",
    "Active D-Lighting": "D-Lighting النشط",
    "Picture Control": "التحكم في الصورة",
    "Exposure Difference": "فرق التعرض",
    "Lens Type": "نوع العدسة",
    "Focus Mode": "وضع التركيز",
    "AF Point": "نقطة التركيز التلقائي",
    "Focus Position": "موضع التركيز",
    "Scaling Factor 35efl": "عامل القياس 35efl",
    "Sharpness Applied To": "الحدة المطبقة على",
    "Noise Reduction": "تقليل الضوضاء",
    "Color Mode": "وضع اللون",
    "Tone Mode": "وضع النغمة",
    "Lightness": "السطوع",
    "Shadows": "الظلال",
    "Highlights": "الإبرازات",
    "Contrast(2)": "التباين (2)",
    "Saturation(2)": "التشبع (2)",
    "Sharpness(2)": "الحدة (2)",
    "Hue": "درجة اللون",
    "Filter Effect": "تأثير الفلتر",
    "GPS Position": "موقع GPS",
    "GPS Date/Time": "تاريخ/وقت GPS",
    "GPS Altitude": "ارتفاع GPS",
    "GPS Speed": "سرعة GPS",
    "GPS Track": "مسار GPS",
    "GPS Image Direction": "اتجاه صورة GPS",
    "GPS Map Datum": "مرجع خريطة GPS",
    "GPS Processing Method": "طريقة معالجة GPS",
    "GPS Area Information": "معلومات منطقة GPS",
    "GPS Destination Latitude": "خط عرض الوجهة GPS",
    "GPS Destination Longitude": "خط طول الوجهة GPS",
    "GPS Destination Bearing": "اتجاه الوجهة GPS",
    "GPS Destination Distance": "مسافة الوجهة GPS",
    "GPS Differential": "تفاضل GPS",
    "GPS H Positioning Error": "خطأ تحديد المواقع الأفقي GPS",
    "Camera Model Name": "اسم موديل الكاميرا",
    "Camera Serial Number": "الرقم التسلسلي للكاميرا",
    "Lens Serial Number": "الرقم التسلسلي للعدسة",
    "Firmware Version": "إصدار البرنامج الثابت",
    "Internal Serial Number": "الرقم التسلسلي الداخلي",
    "Camera Temperature": "درجة حرارة الكاميرا",
    "Battery Level": "مستوى البطارية",
    "Exposure Time": "وقت التعرض",
    "F Number": "رقم F",
    "ISO Speed Ratings": "تقييمات سرعة ISO",
    "Date Time Original": "تاريخ ووقت الالتقاط الأصلي",
    "Date Time Digitized": "تاريخ ووقت الرقمنة",
    "Sub Sec Time Original": "الوقت الأصلي بالمللي ثانية",
    "Sub Sec Time Digitized": "الوقت الرقمي بالمللي ثانية",
    "Focal Length In 35mm Format": "البعد البؤري بتنسيق 35 مم",
    "Scene Type": "نوع المشهد",
    "Custom Rendered": "عرض مخصص",
    "Interoperability Index": "فهرس التشغيل البيني",
    "Interoperability Version": "إصدار التشغيل البيني",
    "Thumbnail Offset": "إزاحة الصورة المصغرة",
    "Thumbnail Length": "طول الصورة المصغرة",
    "User Comment": "تعليق المستخدم",
    "Components Configuration": "تكوين المكونات",
    "Flashpix Version": "إصدار Flashpix",
    "Image Unique ID": "معرف الصورة الفريد",
    "Compression": "الضغط",
    "Photometric Interpretation": "التفسير الضوئي",
    "Strip Offsets": "إزاحات الشريط",
    "Rows Per Strip": "صفوف لكل شريط",
    "Strip Byte Counts": "عدد بايتات الشريط",
    "XMP Toolkit": "مجموعة أدوات XMP",
    "Creator Tool": "أداة الإنشاء",
    "Metadata Date": "تاريخ بيانات التعريف",
    "Document ID": "معرف المستند",
    "Instance ID": "معرف المثيل",
    "Original Document ID": "معرف المستند الأصلي",
    "Format": "التنسيق",
    "Description": "الوصف",
    "Subject": "الموضوع",
    "Keywords": "الكلمات المفتاحية",
    "Rating": "التقييم",
    "Rights": "الحقوق",
    "Creator": "المنشئ",
    "Date Created": "تاريخ الإنشاء",
    "SourceFile": "ملف المصدر",
    "ExifToolVersion": "إصدار ExifTool",
    "FileName": "اسم الملف",
    "Directory": "المجلد",
    "FileSize": "حجم الملف",
    "FileModifyDate": "تاريخ تعديل الملف",
    "FileAccessDate": "تاريخ الوصول إلى الملف",
    "FileCreateDate": "تاريخ إنشاء الملف",
    "FileInodeChangeDate": "تاريخ تغيير عقدة الملف",
    "FilePermissions": "أذونات الملف",
    "FileType": "نوع الملف",
    "FileTypeExtension": "امتداد نوع الملف",
    "MIMEType": "نوع MIME",
    "ExifByteOrder": "ترتيب بايتات Exif",
    "Make": "الشركة المصنعة",
    "Model": "الموديل",
    "Orientation": "الاتجاه",
    "XResolution": "دقة X",
    "YResolution": "دقة Y",
    "ResolutionUnit": "وحدة الدقة",
    "Software": "البرنامج",
    "DateTimeOriginal": "تاريخ ووقت الالتقاط الأصلي",
    "CreateDate": "تاريخ الإنشاء",
    "ModifyDate": "تاريخ التعديل",
    "Artist": "الفنان",
    "Copyright": "حقوق النشر",
    "ExposureTime": "وقت التعرض",
    "FNumber": "رقم F",
    "ExposureProgram": "برنامج التعرض",
    "ISOSpeedRatings": "تقييمات سرعة ISO",
    "SensitivityType": "نوع الحساسية",
    "RecommendedExposureIndex": "مؤشر التعرض الموصى به",
    "ExifVersion": "إصدار Exif",
    "DateTimeDigitized": "تاريخ ووقت الرقمنة",
    "ComponentsConfiguration": "تكوين المكونات",
    "CompressedBitsPerPixel": "البتات المضغوطة لكل بكسل",
    "ShutterSpeedValue": "قيمة سرعة الغالق",
    "ApertureValue": "قيمة فتحة العدسة",
    "ExposureBiasValue": "قيمة تعويض التعرض",
    "MaxApertureValue": "أقصى قيمة لفتحة العدسة",
    "MeteringMode": "وضع القياس",
    "LightSource": "مصدر الضوء",
    "Flash": "الفلاش",
    "FocalLength": "البعد البؤري",
    "SubSecTime": "الوقت بالمللي ثانية",
    "SubSecTimeOriginal": "الوقت الأصلي بالمللي ثانية",
    "SubSecTimeDigitized": "الوقت الرقمي بالمللي ثانية",
    "FlashpixVersion": "إصدار Flashpix",
    "ColorSpace": "مساحة اللون",
    "ExifImageWidth": "عرض صورة Exif",
    "ExifImageHeight": "ارتفاع صورة Exif",
    "InteroperabilityOffset": "إزاحة التشغيل البيني",
    "SensingMethod": "طريقة الاستشعار",
    "SceneType": "نوع المشهد",
    "CustomRendered": "عرض مخصص",
    "ExposureMode": "وضع التعرض",
    "WhiteBalance": "توازن اللون الأبيض",
    "DigitalZoomRatio": "نسبة التكبير الرقمي",
    "FocalLengthIn35mmFormat": "البعد البؤري بتنسيق 35 مم",
    "SceneCaptureType": "نوع التقاط المشهد",
    "GainControl": "التحكم في الكسب",
    "Contrast": "التباين",
    "Saturation": "التشبع",
    "Sharpness": "الحدة",
    "SubjectDistanceRange": "نطاق مسافة الهدف",
    "ImageUniqueID": "معرف الصورة الفريد",
    "GPSVersionID": "إصدار GPS",
    "GPSLatitudeRef": "مرجع خط العرض GPS",
    "GPSLatitude": "خط العرض GPS",
    "GPSLongitudeRef": "مرجع خط الطول GPS",
    "GPSLongitude": "خط الطول GPS",
    "GPSAltitudeRef": "مرجع الارتفاع GPS",
    "GPSAltitude": "الارتفاع GPS",
    "GPSTimeStamp": "الطابع الزمني GPS",
    "GPSDateStamp": "الطابع الزمني لتاريخ GPS",
    "GPSPosition": "موقع GPS",
    "LensInfo": "معلومات العدسة",
    "LensMake": "صانع العدسة",
    "LensModel": "موديل العدسة",
    "LensSerialNumber": "الرقم التسلسلي للعدسة",
    "LensID": "معرف العدسة",
    "Composite": "مركب",
    "ImageSize": "حجم الصورة",
    "Megapixels": "ميغابكسل",
    "ScaleFactor35efl": "عامل القياس 35efl",
    "ShutterSpeed": "سرعة الغالق",
    "DOF": "عمق المجال",
    "FOV": "مجال الرؤية",
    "LightValue": "قيمة الضوء",
    "CircleOfConfusion": "دائرة التشويش",
    "HyperfocalDistance": "مسافة التركيز المفرط",
    "ThumbnailImage": "صورة مصغرة"
}

def translate_key(key):
    return translation_dict.get(key, key)

def extract_metadata(image_path):
    """
    
    """
    if not os.path.exists(image_path):
        print(f"\033[91mخطأ: الملف غير موجود - {image_path}\033[0m") # أحمر
        return None

    try:
        command = ["exiftool", "-json", image_path]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        metadata = json.loads(result.stdout)
        return metadata[0] if metadata else {}
    except subprocess.CalledProcessError as e:
        print(f"\033[91mخطأ في استدعاء exiftool: {e}\033[0m") # أحمر
        print(f"\033[91mالخطأ القياسي: {e.stderr}\033[0m") # أحمر
        return None
    except json.JSONDecodeError:
        print("\033[91mخطأ: فشل تحليل مخرجات JSON من exiftool. قد يكون الملف تالفًا أو غير مدعوم.\033[0m") # أحمر
        return None
    except FileNotFoundError:
        print(f"\033[91mخطأ: لم يتم العثور على exiftool. يرجى التأكد من تثبيته.\033[0m") # أحمر
        return None

def display_and_save_metadata(metadata, output_dir=".", filename_prefix="metadata"):
    """
    
    """
    if not metadata:
        print("لا توجد بيانات تعريف لاستخراجها.")
        return

    os.makedirs(output_dir, exist_ok=True)

    
    logo_and_rights = """
  ███████╗███████╗
  ██╔════╝██╔════╝
  █████╗  ███████╗
  ██╔══╝  ╚════██║
  ██║     ███████║
  ╚═╝     ╚══════╝

  FsociteyF - Professional Exiftool Metadata Extractor

========================================================================
    """

    # بالإنجليزية
    english_output_path = os.path.join(output_dir, f"{filename_prefix}_en.txt")
    with open(english_output_path, "w", encoding="utf-8") as f:
        f.write(logo_and_rights) 
        f.write("\n--- English Metadata ---\n\n")
        for key, value in metadata.items():
            line = f"{key:<30}: {value}\n"
            print(line, end="") # عرض على الشاشة
            f.write(line)
    print(f"\nتم حفظ بيانات التعريف بالإنجليزية في: {english_output_path}\033[0m")

    # بالعربية
    arabic_output_path = os.path.join(output_dir, f"{filename_prefix}_ar.txt")
    with open(arabic_output_path, "w", encoding="utf-8") as f:
        f.write(logo_and_rights)
        f.write("\n--- بيانات التعريف العربية ---\n\n")
        for key, value in metadata.items():
            translated_key = translate_key(key)
            line = f"{translated_key:<30}: {value}\n"
            f.write(line)
    print(f"تم حفظ بيانات التعريف بالعربية في: {arabic_output_path}\033[0m")

if __name__ == "__main__":
    
    print("\033[92m") # 
    print("  ███████╗███████╗")
    print("  ██╔════╝██╔════╝")
    print("  █████╗  ███████╗")
    print("  ██╔══╝  ╚════██║")
    print("  ██║     ███████║")
    print("  ╚═╝     ╚══════╝")
    print("\n  FsociteyF - Professional Exiftool Metadata Extractor")
    print("\033[0m") # 
    print("========================================================================")

    parser = argparse.ArgumentParser(
        description="أداة احترافية لاستخراج بيانات التعريف (metadata) من الصور باستخدام exiftool.",
        epilog="حقوق FsociteyF - جميع الحقوق محفوظة."
    )
    parser.add_argument("image_path", nargs="?", help="المسار إلى ملف الصورة (اختياري).")
    parser.add_argument("-o", "--output_dir", default=".",
                        help="دليل الإخراج لحفظ الملفات النصية (الافتراضي: الدليل الحالي).")
    parser.add_argument("-p", "--prefix", default="metadata",
                        help="بادئة اسم الملف لملفات الإخراج (الافتراضي: metadata).")

    args = parser.parse_args()

    image_file = args.image_path

    if not image_file:
        image_file = input("الرجاء إدخال مسار الصورة: ")

    metadata = extract_metadata(image_file)
    if metadata:
        display_and_save_metadata(metadata, args.output_dir, args.prefix)



