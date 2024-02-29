from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    try: 
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="calendario"
        )
    except mysql.connector.Error as err:
        print(err)
        return None
    else:
        print("Connected to the database")
        return mydb

@app.route('/')
def index():
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM eventos ORDER BY eve_date ASC")
    result = mycursor.fetchall()
    return render_template('index.html', events=result)

if __name__ == '__main__':
    app.run(debug=True)
