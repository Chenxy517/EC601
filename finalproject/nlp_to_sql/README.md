# EC601 Course Project
## Introduction
This project can parse the natural input language and transform it into corresponding SQL language based on a given database. It consists of three main parts: communicator, natural language analyzer and SQL generator. Communicator is the tool of communicating with clients. It can do simple greeting and receive command from clients. Natural language analyzer is the most important part in this project. It is constructed based on Stanford NLP tools, including parser, tagger, tokenizer and grammar classifier. The Stanford tools help to separate the natural language into several logic parts and prepare for the model training and generating SQL. Then SQL generator will train the Stanford NLP models based on a given SQL database. When deviation is lower than 0.1%(which usually is completed within 20 times of training), the model is ready for generating SQL. The SQL generator can look for the keywords in natural language input from the nodes, then transform and recombine these logic parts into SQL queries. 
## MVP
Takes in natural language, and return SQL language according to specific SQL database.
## User Stories
I am a engineer that has never learned SQL before. Now I want to query a SQL database with natural language.
## Test Result
This is a simple result of test based on a local SQL database:

Firstly, Stanford NLP tools need to be downloaded and extracted.

![image](https://github.com/Chenxy517/EC601/blob/main/finalproject/img/test_result_1.png)

Secondly, train the NLP models with given database until deviation is stablized.

![image](https://github.com/Chenxy517/EC601/blob/main/finalproject/img/test_result_2.png)

Finally, clients can post any natural language questions to the program and get a corresponding SQL query.

![image](https://github.com/Chenxy517/EC601/blob/main/finalproject/img/test_result_3.png)
