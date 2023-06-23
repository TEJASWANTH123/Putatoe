from flask import render_template, request
from flask import Blueprint
from flask_mysqldb import MySQL

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin_portal():
    if request.method == 'POST':
        new_word = request.form['new_word']
        mysql = MySQL()  # Create a new MySQL instance
        cur = mysql.connection.cursor()
        cur.execute("UPDATE content SET text = %s", (new_word,))
        mysql.connection.commit()
        cur.close()

    mysql = MySQL()  # Create a new MySQL instance
    cur = mysql.connection.cursor()
    cur.execute("SELECT text FROM content")
    result = cur.fetchone()
    cur.close()

    if result:
        word = result[0]
    else:
        word = 'Word not found'

    return render_template('admin.html', word=word)
