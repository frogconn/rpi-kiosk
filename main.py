from flask import (
    Flask,
    jsonify
)
from flask_cors import CORS

# Create the application instance
app = Flask(__name__,)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# Create a URL route in our application for "/"
@app.route("/api/v1/users")
def home():
    return jsonify([{'name':'frogconn'}])

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
