from bs4 import BeautifulSoup
import requests

# 크롤링할 url
url = "https://www.yes24.com/Main/default.aspx?airbridge_referrer=airbridge%3dtrue%26channel%3dgoogle.adwords%26campaign%3d23080525384%26campaign_id%3d23080525384%26ad_group%3d186378596397%26ad_group_id%3d186378596397%26ad_creative%3d776958993835%26ad_creative_id%3d776958993835%26term%3d%3f%u0080%3f%3f%uc4fd%uf9ce%uc495%uc609%u8084%uc495%u2501%26sub_id%3dg%26sub_id_1%3d%26sub_id_2%3d%26sub_id_3%3db%26click_id%3dCjwKCAjwqubPBhBOEiwAzgZX2j49KVrf0uvNLepLOZK1kFKE2hCMHMWsph0wsNXzQGVqEyj80i4YrxoCf5IQAvD_BwE%26gclid%3dCjwKCAjwqubPBhBOEiwAzgZX2j49KVrf0uvNLepLOZK1kFKE2hCMHMWsph0wsNXzQGVqEyj80i4YrxoCf5IQAvD_BwE%26ad_type%3dclick&gad_source=1&gad_campaignid=23080525384&gbraid=0AAAAAD79IrrWVd12gYS0BHxDh1en1ceJ6&gclid=CjwKCAjwqubPBhBOEiwAzgZX2j49KVrf0uvNLepLOZK1kFKE2hCMHMWsph0wsNXzQGVqEyj80i4YrxoCf5IQAvD_BwE"
# 결과값 받아오기
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# 실행
print(soup.prettify)


# find
print("----   find   ----")
print(soup.find("a"))
# find all
print(soup.find_all("h4"))

# select
print("----   select   ----")
print(len(soup.select("h3")))

# 응용 헤드라인 추출
print("----   해드라인추출결과   ----")
headlines = soup.select(".tB_readTit")
for headline in headlines:
    print(headline.text.strip())