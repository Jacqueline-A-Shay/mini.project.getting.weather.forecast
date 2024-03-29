import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page

from bs4 import BeautifulSoup as BS
soup = BS(page.content, 'html.parser')
# print(soup.prettify())


page = requests.get("http://forecast.weather.gov/MapClick.php?lat=29.46&lon=-98.5")
soup = BS(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)


period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# periods

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# print(short_descs)
# print(temps)
# print(descs)


import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
print(weather)
print("a-okay")
"""
temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
temp_nums


weather["temp_num"].mean()

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
is_night

weather[is_night]
"""
