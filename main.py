from flask import Flask, jsonify
import sqlite3
import random

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_db_connection()
    with app.open_resource('script_database.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

initialize_database()


def get_quote_by_topic(topic):
    conn = get_db_connection()
    quotes = conn.execute("SELECT Quote.text, Quote.author FROM Quote JOIN QuoteTopic ON Quote.id = QuoteTopic.quote_id JOIN Topic ON QuoteTopic.topic_id = Topic.id WHERE Topic.topic = ?;", (topic,)).fetchall()
    conn.close()
    if not quotes:
        return jsonify({'error': 'No quotes found'}, 404)
    random_quote = random.choice(quotes)
    return jsonify(dict(random_quote))

@app.route('/quote/<string:topic>', methods=['GET'])
def get_quote(topic):
    return get_quote_by_topic(topic)

if __name__ == '__main__':
    app.run(debug=False)
