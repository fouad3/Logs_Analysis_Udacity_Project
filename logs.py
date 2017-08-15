#! /usr/bin/env python3

# Import Postgres sql library
import psycopg2

# Store global database name
DBNAME = "news"


"""
Here I've listed the VIEWS I created within the news database
to answer the below-listed problem sets

For Problem 1,Problem2:
CREATE VIEW top_views AS
SELECT title,author,count(*) AS views
FROM articles,log
WHERE log.path like concat('%',articles.slug)
GROUP BY title,author
ORDER BY views desc;

For Problem3:
CREATE VIEW all_status AS
SELECT time::timestamp::date AS date,count(log.status) AS num
FROM log
GROUP BY date
ORDER BY num desc;

CREATE VIEW false_status AS
SELECT time::timestamp::date AS date,count(log.status) num
FROM log
WHERE status!='200 OK'
GROUP BY date
ORDER BY num desc;
"""

# 1. What are the most popular three articles of all time?
query1 = """SELECT title,views
          FROM top_views
          LIMIT 3; """


# 2. Who are the most popular article authors of all time?
query2 = """SELECT authors.name,SUM(top_views.views) AS author_view
          FROM authors,top_views
          WHERE authors.id=top_views.author
          GROUP BY authors.id
          ORDER BY author_view DESC;
"""

# 3. On which days did more than 1% of requests lead to errors?
query3 = """SELECT false_status.date,round(100.0*false_status.num / all_status.num,2)
          AS error
          FROM all_status,false_status
          WHERE false_status.date=all_status.date
          AND round(100.0*false_status.num / all_status.num,2)>1
          ORDER BY error DESC;"""


def popular_article(query1):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("%s --> %d" % (title, views))
    db.close()


def popular_authors(query2):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query2)
    results = c.fetchall()
    for i in range(len(results)):
        name = results[i][0]
        views = results[i][1]
        print("%s --> %d" % (name, views))
    db.close()


def error_percent(query3):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query3)
    results = c.fetchall()
    for i in range(len(results)):
        date = results[i][0]
        error = results[i][1]
        print("%s --> %.1f %%" % (date, error))
    db.close()


# Print results of queries
print("Most popular three articles of all time:")
popular_article(query1)
print("\n")
print("Most popular article authors of all time:")
popular_authors(query2)
print("\n")
print("Days with more than 1% of requests lead to errors:")
error_percent(query3)
