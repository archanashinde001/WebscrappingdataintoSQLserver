# WebscrappingdataintoSQLserver
Webscraping using Beautiful soup python library and saving the data in SQL server table 

The code shows how to connect Python with SQL server by creating a table in SQL server with help of create_table.py. But before creating the table make sure to create a database which you wish to connect.


Once we create the table in the SQL server, the next step is to web-scrap data from the site. Before web scraping data make sure you read the robot.txt of that website and see if you are allowed to web scrap the data from the website. Once you finalize the website, you can use Data_collection_normal.py to fetch the data from the website and insert the data in the SQL server table. 


For web scraping, I have used the beautifulsoup python library, which is very easy to understand and implement.
