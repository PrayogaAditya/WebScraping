import requests
from bs4 import BeautifulSoup
import pd



url = "https://techcrunch.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


article_titles, article_contents, article_hrefs = [], [], []
for tag in soup.findAll("div", {"class": "post-block post-block--image post-block--unread"}):
    tag_header = tag.find("a", {"class": "post-block__title__link"})
    tag_content = tag.find("div", {"class": "post-block__content"}) 
    article_title = tag_header.get_text().strip()
    article_href = tag_header["href"]
    article_content = tag_content.get_text().strip()
    article_titles.append(article_title)
    article_contents.append(article_content)
    article_hrefs.append(article_href)

df = pd.DataFrame({"title": article_titles, "content": article_contents, "href": article_hrefs})



def auto_adjust_excel_columns(worksheet, df):
    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]
        max_len = (
            max((
series.astype(str).map(len).max(),  # len of largest item
len(str(series.name)),  # len of column name/header
                )
            )
            + 1
        )  # adding a little extra space
        worksheet.set_column(idx, idx, max_len)  # set column width



writer = pd.ExcelWriter('TechCrunch_latest_news.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
auto_adjust_excel_columns(writer.sheets['Sheet1'], df)
writer.save()


