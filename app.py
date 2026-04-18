data = {
    "خفيف": {
        "اعراض": """
نسيان الأحداث القريبة (مواعيد، أسماء)
تكرار الأسئلة
صعوبة في التركيز والانتباه
ضياع بسيط في الأماكن المألوفة
بداية صعوبة في التعبير بالكلمات
""",

        "علاج دوائي": """
مثبطات إنزيم الكولين إستيراز:
Donepezil
Rivastigmine
Galantamine

الهدف: تحسين الوظائف المعرفية وإبطاء التدهور
""",

        "تكفل نفسي": """
التدخل المعرفي (CST)
الدعم الانفعالي
التثقيف النفسي
تعزيز الكفاءة الذاتية
تنشيط التفاعل الاجتماعي
""",

        "صورة": r"C:\Users\pc\AppData\Local\Programs\Python\Python311\Alzheimers-project\dataset\mild.jpg"
    },

    "متوسط": {
        "اعراض": """
نسيان واضح ومتكرر للأحداث اليومية
صعوبة في تذكّر الأسماء والأشخاص
ارتباك في الزمان والمكان
تكرار نفس الكلام
صعوبة في الكلام والتعبير
تغيرات في السلوك
""",

        "علاج دوائي": """
مثبطات الكولين إستيراز:
Donepezil
Rivastigmine
Galantamine

+ Memantine

الهدف: تقليل التدهور وتحسين السلوك
""",

        "تكفل نفسي": """
Reality Orientation Therapy
Reminiscence Therapy
Behavioral Management
Environmental Structuring
Family Counseling
""",

        "صورة": r"C:\Users\pc\AppData\Local\Programs\Python\Python311\Alzheimers-project\dataset\moderate.jpg"
    },

    "شديد": {
        "اعراض": """
فقدان شبه كامل للذاكرة
عدم التعرف على العائلة
فقدان القدرة على الكلام
صعوبة في الحركة
اعتماد كامل على الآخرين
""",

        "علاج دوائي": """
Memantine

قد يستخدم Donepezil

مضادات الذهان بحذر
مهدئات
مسكنات ألم

الهدف: تحسين جودة الحياة
""",

        "تكفل نفسي": """
Person-Centered Care
Non-verbal Communication
Sensory Stimulation
Distress Reduction
Caregiver Support
""",

        "صورة": r"C:\Users\pc\AppData\Local\Programs\Python\Python311\Alzheimers-project\dataset\severe.jpg"
    }
}

# =========================

from PIL import Image

while True:
    level = input("اكتب المستوى (خفيف / متوسط / شديد أو خروج): ")

    if level == "خروج":
        print("تم إيقاف البرنامج")
        break

    if level in data:
        img = Image.open(data[level]["صورة"])
        img.show()

        while True:
            choice = input("ماذا تريد؟ (اعراض / علاج دوائي / تكفل نفسي / رجوع): ")

            if choice == "رجوع":
                break

            if choice in data[level]:
                print("\n" + data[level][choice])
            else:
                print("خيار غير صحيح")
    else:
        print("مستوى غير صحيح")
