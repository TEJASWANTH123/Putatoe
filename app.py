from flask import Flask
from flask_mysqldb import MySQL
from routes.admin import admin_bp
from routes.api import api_bp

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'employee'

mysql = MySQL(app)

app.register_blueprint(admin_bp)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run()
