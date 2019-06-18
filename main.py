import RPi.GPIO as GPIO
from time import sleep
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
    GPIO.setwarnings(False)    # Ignore warning
    GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(8, GPIO.HIGH) # Turn on
    sleep(2)                  # Sleep for 1 second
    GPIO.output(8, GPIO.LOW)  # Turn off
    return jsonify([{'name':'frogconn'}])

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
