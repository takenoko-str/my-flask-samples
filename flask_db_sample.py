import json
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sakila'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/id/<num>', methods=['GET'])
def users(num):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('select title, description from film where film_id = {}'.format(num))
        rv = cur.fetchall()
        return json.dumps(rv, indent=4)


if __name__ == '__main__':
    app.run()

