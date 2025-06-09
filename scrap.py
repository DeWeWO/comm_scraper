from google_play_scraper import Sort, reviews
import pandas as pd

# Ilova ID'si
app_id = "org.telegram.messenger" 

result, _ = reviews(
    app_id,
    lang='uz',      # Izohlar qaysi tilda bo‘lishi
    country='us',
    sort=Sort.NEWEST,
    count=100       # Nechta izoh yuklansin
)

# Faqat yulduzlar va izoh matnlarini ajratib olish
data = [{'score': r['score'], 'content': r['content']} for r in result]

df = pd.DataFrame(data)

df.to_csv("tg_comm.csv", index=False, encoding='utf-8-sig')

print(".csv faylga comment lar saqlandi.")





