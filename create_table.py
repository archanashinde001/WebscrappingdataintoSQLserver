
import pyodbc #improting python library which will help to connect with sql database

#Establish connection with MS SQL server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=******;' #your PC name
                      'Database=SampleDB;'
                      'Trusted_Connection=yes;')           


cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE Review_detail
               (
               Review_id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
               UserName varchar(100) NOT NULL,
               UserLocation varchar(100),
               Review_date varchar(100),
               Title varchar(1000) NOT NULL,
               Bodytext varchar(MAX) NOT NULL,
               Ratings varchar(100) NOT NULL,
               URl varchar(100) NOT NULL,
               )
               ''')

conn.commit()
conn.close()

  