from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
import time

message_bp = Blueprint('message_bp', __name__)

@message_bp.route('/', methods=['GET'])
def global_feed():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, user_id INT, content TEXT, timestamp INT)")
    c.execute('SELECT messages.content, users.username FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.timestamp DESC')
    messages = c.fetchall()
    conn.close()
    
    return render_template('index.html', messages=messages)

@message_bp.route('/message', methods=['POST'])
def post_message():
    content = request.form['content']
    username = request.form['username']
    
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('SELECT id FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    
    if user:
        user_id = user[0]
        c.execute('INSERT INTO messages (user_id, content, timestamp) VALUES (?, ?, ?)', (user_id, content, int(time.time())))
        conn.commit()
    conn.close()
    
    return redirect(url_for('message_bp.global_feed'))
