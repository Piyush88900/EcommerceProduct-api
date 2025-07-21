from flask import Flask, jsonify 
import mysql.connector 
import os #

app = Flask(__name__) 

# MySQL Config from environment variables (passed via Docker)
DB_HOST = os.environ.get('MYSQL_HOST', 'db')
DB_USER = os.environ.get('MYSQL_USER', 'root')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'root')
DB_NAME = os.environ.get('MYSQL_DATABASE', 'producthub')

# Route: /products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to ProductHub API'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
