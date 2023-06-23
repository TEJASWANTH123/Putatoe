from flask import Blueprint
from flask_mysqldb import MySQL

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/test', methods=['GET'])
def get_test_word():
    mysql = MySQL()  # Create a new MySQL instance
    cur = mysql.connection.cursor()
    cur.execute("SELECT text FROM content")  # Assuming a table named 'content' with 'text' column
    result = cur.fetchone()
    cur.close()

    if result:
        return result[0]
    else:
        return 'Word not found'
