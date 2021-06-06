import re
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import pyodbc


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

base_url= "https://www.****" #website to scrap. I had used trustpilot website to web scrap amazon.com reviews
pagesToGet=5
records=[] 
#Establish connection with MS SQL server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=******;'
                      'Database=SampleDB;'
                      'Trusted_Connection=yes;')           


cursor = conn.cursor()


def get_review_det(url):
        count=0
        url_pattern=requests.get(url,headers=headers)
        url_data = BeautifulSoup(url_pattern.text, 'html.parser') 
        reviews=url_data.find_all('article', attrs={'class':'review'})
        for review in reviews:
            username=review.find('div', class_="consumer-information__name").text.strip()   
            user_location=review.find('div', class_="consumer-information__location").text.strip()
            date_container=str(review.find('div', class_="review-content-header__dates"))
            review_date=date_container.split(':"')[1].split('",')[0]
            title=review.find('h2', attrs={'class':'review-content__title'}).text.strip()
            body=review.find('p', attrs={'class':'review-content__text'}).text.strip()
            rating=review.find('img')['alt']
            records.append((username,user_location,review_date,title,body,rating))
            cursor.execute("INSERT INTO SampleDB.dbo.Review_details(UserName,UserLocation,Review_date,Title,Bodytext,Ratings)\
                VALUES (?,?,?,?,?,?)",username,user_location,review_date,title,body,rating)
            conn.commit()
        return(records)


start = time.time()
for page in range(1,pagesToGet+1):
        url = base_url+'?page='+str(page)
        output=get_review_det(url)
print("Total number of rows inserted: ",len(output))
end =time.time()
Total= end-start
print("Overall time of execution: ", Total)
conn.close()