# assignment4md4

There are two Python files in this PyCharm project: main.py and app.py. 
They have been created in response to this assignment (main.py for assignment 1 and app.py for assignment 2):
 
1. Please write a program to fetch data stored in 2 PDF files. To help you with your assignment our magic parser have converted these files to Excel files. They are available under "xlsx" directory. Your task is to write a program which will extract data from Excel files.

We will need the following info for each page in a document:

  1) data stored under first column "This Yr", except lines containing string "Total".
    For "investor-weekly-carloads-august-2016.pdf" that would be:
      "All Other Carloads": 746
      "Chemicals": 7762
      ...
      "Coal": 15906
      "Coke": 1,274
      (for every page)

  2) the start and the end of the week for that data.
    At the top of every page we have the following line:
    "Week 31 (Q3) From: 07-31-2016 To: 08-06-2016"

    Please store "07-31-2016" (start of the week) and "08-06-2016" (end of the week) together with data.


Collected data should be stored locally using a method you prefer.

Note: For parsing Excel files you may use
https://openpyxl.readthedocs.io/en/stable/
or whatever library you prefer.

2. Please write a second program that will start an API web-service on port 8080 (use flask) that will return the stored data

Create an endpoint that will accept HTTP GET with following arguments:
  * week_start - required (iso format like 2017-05-10)
  * week_end - required (iso format like 2017-05-22)
and return data for specified time period.

example of calling by using curl:
  curl 'http://127.0.0.1:8080/data?week_start=2017-05-10&week_end=2017-05-22'

example of output data:

  {
      "All Other Carloads": 746
      "Chemicals": 7762
      "Coal": 15906
      "Coke": 1274,
      ...
      "week_start": "2017-05-10",
      "week_end": "2017-05-22",
  }


All services should be running in Docker.
