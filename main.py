from flask import Flask
from routes.user import user_bp
from routes.message import message_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(message_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
