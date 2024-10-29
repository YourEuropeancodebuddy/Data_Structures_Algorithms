import RPi.GPIO as GPIO
import time

# Define GPIO pins
echo = 6
trig = 7
led = 8
buzzer = 9

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(trig, GPIO.LOW)
GPIO.output(led, GPIO.LOW)
GPIO.output(buzzer, GPIO.LOW)
time.sleep(2)  # Give time to stabilize

print("Ultrasonic Measurement")

try:
    while True:
        # Send an impulse to trigger the sensor start the measurement
        GPIO.output(trig, GPIO.HIGH)
        time.sleep(0.000015)  # Minimum impulse width required by HC-SR04 sensor
        GPIO.output(trig, GPIO.LOW)
        
        # Wait until the sensor outputs the result
        while GPIO.input(echo) == GPIO.LOW:
            pulse_start = time.time()
        while GPIO.input(echo) == GPIO.HIGH:
            pulse_end = time.time()

        # Calculate duration
        pulse_duration = pulse_end - pulse_start

        # Calculate distance
        vsound = 340  # m/s
        distance = (pulse_duration / 2) * vsound * 100  # Convert to cm

        if distance > 500 or distance < 2:
            print("Invalid range!")
        else:
            print("Distance:", distance, "cm")

        # Light up the LED and buzz the buzzer if the distance is less than 50 cm
        if distance < 50:
            GPIO.output(led, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.HIGH)
        else:
            GPIO.output(led, GPIO.LOW)
            GPIO.output(buzzer, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
