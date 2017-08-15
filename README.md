# Project : Logs Analysis
## By  Fouad Asharf



## Table of contents
- [Description](#description)
- [Required Libraries and Dependencies](#required-libraries-and-dependencies)
- [How to Run Project](#how-to-run-project)
- [Project contents](#project-contents)
- [Copyright and license](#copyright-and-license)
 
## Description
This is a logs analysis project which is internal reporting tool that will use information from the database to discover what kind of articles the site's readers like,this project is a part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Required Libraries and Dependencies
 1. Install python 3.x, you can Download it from https://www.python.org/.
 1. Install Vagrant, you can download it from https://www.vagrantup.com/.
 2. Install  VirtualBox, you can download it from https://www.virtualbox.org/.
 2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
 3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
 4. Unzip this file after downloading it. The file inside is called newsdata.sql.

## How to Run Project
1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
3. Change directory to /vagrant and look around with ls.
4. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
5. Use `psql -d news` to connect to database.
 
6. Create view top_views using:
   ```
CREATE VIEW top_views AS
SELECT title,author,count(*) AS views
FROM articles,log
WHERE log.path like concat('%',articles.slug)
GROUP BY title,author
ORDER BY views desc;
  ```
   | Column  | Type    |
   | :-------| :-------|
   | title   | text    |
   | author  | text    |
   | views   | Integer |
  


7.Create view all_status using:

   ```
CREATE VIEW all_status AS
SELECT time::timestamp::date AS date,count(log.status) AS num
FROM log
GROUP BY date
ORDER BY num desc;
  ```
   | Column  | Type    |
   | :-------| :-------|
   | date    | date    |
   | num     | Integer |
  

8.Create view false_status using:

   ```
CREATE VIEW false_status AS
SELECT time::timestamp::date AS date,count(log.status) num
FROM log
WHERE status!='200 OK'
GROUP BY date
ORDER BY num desc;
  ```
   | Column  | Type    |
   | :-------| :-------|
   | date    | date    |
   | num     | Integer |
9. From the vagrant directory inside the virtual machine,run logs.py using:
  ```
    $ python3 logs.py
  ```


## Project contents

##### popular_article method
Function in [logs.py](https://github.com/fouad3/Logs_Analysis_udacity_project/blob/master/logs.py) file used for processing query1 to get most popular three articles of all time and print query1 resluts
like sample output in [sampled_output.txt](https://github.com/fouad3/Logs_Analysis_udacity_project/blob/master/sample_output.txt) file.
##### popular_authors method
Function in [logs.py](https://github.com/fouad3/Logs_Analysis_udacity_project/blob/master/logs.py) file  used for processing query2 to get popular article authors of all time and print query2 resluts
like sample output in [sampled_output.txt](https://github.com/fouad3/Logs_Analysis_udacity_project/blob/master/sample_output.txt) file.

##### error_percent method
Function in [logs.py](https://github.com/fouad3/Logs_Analysis_udacity_project/blob/master/logs.py) file used for processing query3 to get days with more than 1% of requests lead to errors 
and print query3 resluts like sample output in [sampled_output.txt](https://github.com/fouad3/Logs_Analysis_udacity_project/blob/master/sample_output.txt) file.


## Copyright and License

- supplied without rights information contributed by [Udacity](http://www.udacity.com).
