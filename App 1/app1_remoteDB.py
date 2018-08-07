import mysql.connector


word = input("Enter a English word: ")

con = mysql.connector.connect(user='ardit700_student', password='ardit700_student', host='108.167.140.122', database='ardit700_pm1database')
cur = con.cursor()
query = cur.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cur.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print('Word not found. Try again!')


