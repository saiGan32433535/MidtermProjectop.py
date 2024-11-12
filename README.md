## Kirtitej Gandham

## Midterm Project

## PANDAS PACKAGE

## TV SHOW REC PROJECT

### Package summary:
Pandas is a package that is used to work with any kind of data set. It’s very useful when dealing with large amounts of data. With pandas you can manipulate, clean, and analyze data.  Pandas have a wide  range of functions. It can do simple things such as reading and processing data files. In my case, I used pandas to process a csv file that contains data on all kinds of shows. Pandas is capable of processing these sets of data, and creating its own dataframe. A data frame is a data structure that turns data sets into organized 2d structures that contain rows and columns. This makes it so much easier for data analysis to be carried out. This package is very important in the field of data science and data analytics.  

### Instructions: 
To install this Package you must open your terminal and type pip install pandas. 

**On Windows**
$ python -m pip install pandas

**On Mac**

$ python  pip install pandas

**Note**

Code must also have access to the Csv file on Visual studio code. Folder should contain both the code and file. 


### code explained: 
I always like to find new shows to watch, but I also have a hard time finding new ones. That's why I used this idea for my midterm Project. This code uses the pandas package so that it can use the csv file to create a filtered data frame. The csv file was pulled from kaggle which contains many different shows. This csv file was made from imdb which is a popular website for rating every tv show. When running the code, it will ask the user for what genre they want shows recommended. I defined a function and the first purpose of this function was to filter out the necessary rows from the dataframe. So if the user picks “Action” for example, my code will ensure to only include rows where the genre includes action. It does this by searching for the stated substring values(Action), in the string which is genre. Additionally, my code also filters out lower rated shows. So in this case, the filtered data frame will only contain action shows that are higher rated than 8.8. So by then every row that is not action and not rated higher than 8.8 will be filtered out. The data frame will only contain the necessary values. By the end of the function my code returns only the “Titles” column of all the rows that haven’t been filtered out. After the user asks for their preferred genre, it should print out the recommended shows. 


### Future idea: 

I would say my future idea would be to use pandas  for stock market analysis. More specifically the s&p 500. By collecting large data sets on kaggle and yahoo, I can find data on S&P 500 and different economic factors such as unemployment rate as well as federal interest rates. By using pandas I can most likely combine these data sets together into one dataframe. I can use pandas to do simple tasks such as finding trends. I can also use pandas to identify years where the s&p 500 was performing the best or worst, and correlate it to different economic factors as mentioned before. 


