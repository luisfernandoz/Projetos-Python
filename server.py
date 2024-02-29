from flask import Flask, render_template, request, jsonify
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

mydb = connect_to_database()
mycursor = mydb.cursor()

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM eventos ORDER BY eve_date ASC")
    result = mycursor.fetchall()
    return render_template('index.html', events=result)

@app.route('/delete/<int:event_id>', methods=['POST'])
def deleteEvent(event_id):
    try:
        mycursor.execute("DELETE FROM eventos WHERE eve_id = %s", (event_id,))
        mydb.commit()
        return jsonify({'status': 'success', 'message': 'Event deleted successfully.'})
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': 'Error deleting event.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
