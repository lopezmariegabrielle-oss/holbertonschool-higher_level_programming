import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                products = json.load(file)
        except FileNotFoundError:
            return render_template(
                'product_display.html', error="Data file not found"
            )

    elif source == 'csv':
        try:
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(
                        {
                            'id': int(row['id']),
                            'name': row['name'],
                            'category': row['category'],
                            'price': float(row['price']),
                        }
                    )
        except FileNotFoundError:
            return render_template(
                'product_display.html', error="Data file not found"
            )

    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()

            for row in rows:
                products.append(
                    {
                        'id': row[0],
                        'name': row[1],
                        'category': row[2],
                        'price': row[3],
                    }
                )
            conn.close()
        except sqlite3.Error:
            return render_template(
                'product_display.html', error="Database error"
            )

    if product_id:
        try:
            target_id = int(product_id)
            products = [p for p in products if p['id'] == target_id]

            if not products:
                return render_template(
                    'product_display.html', error="Product not found"
                )
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
