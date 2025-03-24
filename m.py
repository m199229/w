import requests
from bs4 import BeautifulSoup
import pandas as pd

# رابط صفحة الأخبار عن السودان في الجزيرة
url = "https://www.aljazeera.net/where/sudan"

# إرسال طلب للموقع وجلب المحتوى
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# استخراج عناوين الأخبار وروابطها
news_data = []
articles = soup.find_all("article")

for article in articles:
    title = article.find("h3").text.strip() if article.find("h3") else "عنوان غير متوفر"
    link = article.find("a")["href"] if article.find("a") else "رابط غير متوفر"
    
    # حفظ البيانات في قائمة
    news_data.append({"عنوان": title, "رابط": f"https://www.aljazeera.net{link}"})

# تحويل البيانات إلى DataFrame وعرضها
df = pd.DataFrame(news_data)
print(df)

# حفظ البيانات في ملف CSV
df.to_csv("sudan_news_aljazeera.csv", index=False)
