from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/pearl/OneDrive/Desktop/project127/chromedriver.exe")
browser.get(url)
time.sleep(10)

star_data = []
final_star_data = []
header = ["name","distance","mass","radius","luminousity"]
def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")

    bright_star_table = soup.find("table")
    table_tbody = bright_star_table.find("tbody")
    #table_rows = table_tbody.find_all("tr")
    for table_row in table_tbody.find_all("tr"):
        td_tags = table_row.find_all("td")
        temp_list = []
        for index,td_tag in enumerate(td_tags):
                try:
                    temp_list.append(td_tag.text.strip())
                except:
                    temp_list.append("")
        
        star_data.append(temp_list)

scrape()

for i in range(0,len(star_data)):
    Star_names = star_data[i][1] 
    Distance = star_data[i][3] 
    Mass = star_data[i][5] 
    Radius = star_data[i][6] 
    Lum = star_data[i][7]
    details = [Star_names,Distance,Mass,Radius,Lum]  
    final_star_data.append(details)

print(final_star_data)  
    
with open("result.csv","w",encoding="utf8",newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(final_star_data)
    


