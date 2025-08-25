from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Hello from Flask on Railway!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # این خط خیلی خیلی حیاتیه!
    print(f"⚡ Starting Flask app on port: {port} ...")  # لاگ ساده برای تست تو لاگ‌ها
    app.run(host='0.0.0.0', port=port)