import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime
from sqlite3 import Error
def crdb(db_file):
     conn= None
     try:
          conn=sqlite3.connect(db_file)
          return conn
     except Error as e:
          print(e)
     return conn
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def create_task(conn, link_t):
    sql = ''' INSERT INTO links(link_date,link)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, link_t)
    conn.commit()
    return cur.lastrowid

def main():
    var = r"C:\sqlite\python.db"
    data = datetime.date.today()
    result = requests.get("https://www.eurogamer.net/")
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    link = soup.find("a", class_="hitbox")
    nlink = link.attrs['href']
    task=(data, nlink)
    conn = crdb(var)
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS links (
                                            link_date text NOT NULL,
                                            link text NOT NULL
                                        );"""
    create_table(conn, sql_create_tasks_table)
    with conn:
        create_task(conn, task)
if __name__ == '__main__':
    main()