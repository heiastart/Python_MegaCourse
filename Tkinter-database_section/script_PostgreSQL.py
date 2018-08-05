import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='section12_udemy' user='postgres' password='SUdo1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='section12_udemy' user='postgres' password='SUdo1234' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" %(item, quantity, price)) NB: NOT good/BAD -> SQL injection attack!!
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price)) # Better since two separate arguments :)

    conn.commit()
    conn.close()

def view_table():
    conn = psycopg2.connect("dbname='section12_udemy' user='postgres' password='SUdo1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_record(item):
    conn = psycopg2.connect("dbname='section12_udemy' user='postgres' password='SUdo1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update_data(quantity, price, item):
    conn = psycopg2.connect("dbname='section12_udemy' user='postgres' password='SUdo1234' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()

create_table()
insert_data('Appelsin', 15, 20)
#delete_record('Appelsin')
update_data(35,15,'Eple')
print(view_table())