from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        username = request.form['username']
        if not username:
            return "Username is required!", 400
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)")
        c.execute('INSERT INTO users (username) VALUES (?)', (username,))
        conn.commit()
        conn.close()
        
        return redirect(url_for('message_bp.global_feed'))
    
    return render_template('profile.html')
