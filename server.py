from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    try: 
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        print("Connected to the database")
        return mydb
    except mysql.connector.Error as err:
        print("Error connecting to the database:", err)
        return None

mydb = connect_to_database()
mycursor = mydb.cursor()

mycursor.close()

@app.route('/')
def index():
    mydb = connect_to_database()
    if mydb:
        try:
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS calendario")
            mycursor.execute("USE calendario")
            mycursor.execute("CREATE TABLE IF NOT EXISTS eventos (eve_id INT AUTO_INCREMENT PRIMARY KEY, eve_nome VARCHAR(255), eve_desc TEXT, eve_date CHAR(16))")
            mycursor.execute("SELECT * FROM eventos ORDER BY eve_date ASC")
            result = mycursor.fetchall()
            return render_template('index.html', events=result)
        except mysql.connector.Error as err:
            print("Error executing SQL query:", err)
            return render_template('error.html', message="Error fetching events from the database.")
        finally:
            mycursor.close()
            mydb.close()
    else:
        return render_template('error.html', message="Failed to connect to the database.")

@app.route('/delete/<int:event_id>', methods=['POST'])
def deleteEvent(event_id):
    mydb = connect_to_database()
    if mydb:
        try:
            mycursor = mydb.cursor()
            mycursor.execute("USE calendario")
            mycursor.execute("DELETE FROM eventos WHERE eve_id = %s", (event_id,))
            mydb.commit()
            return jsonify({'status': 'success', 'message': 'Event deleted successfully.'})
        except mysql.connector.Error as err:
            print("Error executing SQL query:", err)
            return jsonify({'status': 'error', 'message': 'Error deleting event.'}), 500
        finally:
            mycursor.close()
            mydb.close()
    else:
        return jsonify({'status': 'error', 'message': 'Failed to connect to the database.'}), 500
    
@app.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    description = request.form['description']
    date = request.form['date']

    mydb = connect_to_database()
    if mydb:
        try:
            cursor = mydb.cursor()
            cursor.execute("USE calendario")
            cursor.execute("INSERT INTO eventos (eve_nome, eve_desc, eve_date) VALUES (%s, %s, %s)", (title, description, date))
            mydb.commit()
            cursor.close()    
            return jsonify({'status': 'success', 'message': 'Event created successfully.'})
        except mysql.connector.Error as err:
            print("Error executing SQL query:", err)
            return jsonify({'status': 'error', 'message': 'Error creating event.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
