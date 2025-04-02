import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

# Set up GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # Ensure LED is off initially

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/control', methods=['POST'])
def led_control():
    action = request.form.get('action')
    
    if action == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        status = 'LED is ON'
    elif action == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        status = 'LED is OFF'
    else:
        status = 'Invalid action'
    
    return {'status': status}

@app.route('/led/status')
def led_status():
    status = 'ON' if GPIO.input(LED_PIN) else 'OFF'
    return {'status': status}

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        cleanup()

