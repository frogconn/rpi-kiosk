from flask import (
    Flask,
    jsonify
)

# Create the application instance
app = Flask(__name__,)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return jsonify([{'name':'frogconn'}])

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
