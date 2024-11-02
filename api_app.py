from flask import Flask, render_template_string
import psycopg2

app = Flask(__name__)

# PostgreSQL connection info
conn = psycopg2.connect(
    dbname="dvdrental", 
    user="raywu1990", 
    password="test", 
    host="127.0.0.1", 
    port="5432"
)

@app.route('/api/update_basket_a')
def update_basket_a():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
    conn.commit()
    cursor.close()
    return "Successfully added items to basket"

@app.route('/api/unique')
def unique_fruits():
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT fruit_a FROM basket_a")
    unique_a = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT fruit_b FROM basket_b")
    unique_b = [row[0] for row in cursor.fetchall()]
    cursor.close()

    html = """
    <html>
    <body>
        <h2>Unique Fruits</h2>
        <table border="1">
            <tr><th>Unique in Basket A</th><th>Unique in Basket B</th></tr>
            <tr><td>{}</td><td>{}</td></tr>
        </table>
    </body>
    </html>
    """.format(', '.join(unique_a), ', '.join(unique_b))

    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)

