from flask import Flask, render_template, request
app = Flask(__name__)
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_11", GPIO.IN)

@app.route("/")
def hello():
  if GPIO.input("P8_11"):
    doorstatus = "open"
  else:
    doorstatus = "closed"

  templateData = {
    'doorstatus':doorstatus,
  }
  #Use request.args to get parsed contents of query string:
  thing = request.args.get('thing')
  print thing

  return render_template('main_control.html', **templateData)

#variable  example:
#@app.route("/ledLevel/<level>") #this is a variable 'level'
#def pin_state(level): #(pin):
#  PWM.start(pin, float(duty_cycle))
#  print level

#  return ...

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=1234, debug = True)
