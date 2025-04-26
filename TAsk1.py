import paho.mqtt_client as mqtt
import RPi.GPIO as GPIO
import Adafruiy_DHT
class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):    
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_typ=self.topic_list[2]
        self.name =self.topic_list[3]
        self.mqtt_broker=mqtt_broker
        self.port=port
        self.status='off'
        self.connect_mqtt()
        self.setup_gpio()
    def connect_mqtt(self):
        self.mqtt_client=mqtt.client()
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        
    def setup_gpio(self):
        if self.device_typ=='lamps':
            GPIO.setup(17,GPIO.OUT)
        elif self.device_typ=='door':
            GPIO.setup(27,GPIO.OUT)
        elif self.device_typ=='fans':
            GPIO.setup(22,GPIO.OUT)
#### task1
        elif self.device_typ=='camera':
            GPIO.setup(100,GPIO.OUT)
    def send_commands(self,command):
        self.mqtt.publish(self.topic,command)
        print('don')
            
    def turn_on(self):
        self.mqtt_client.publish(self.topic,'TURN_ON')
        self.status='on'
        print('turn_on')

    def turn_off(self):
        self.mqtt_client.publish(self.topic,'TURN_OFF')
        self.status='off'
        print('turn off')
        
class Sensor:
    def __init__(self,topic,pin=100):
      self.topic=topic
      self.topic_list=self.topic.split('/')
      self.location=self.topic_list[0]
      self.group=self.topic_list[1]
      self.snsor_typ=self.topic_list[2]
      self.sensor_name =self.topic_list[3]   
    def read_sensor(self):
       humidity,temperature=Adafruiy_DHT.red_retry(Adafruiy_DHT,self.pin)
       if self.sensor_type== 'thermoset':
           return temperature
       else:
           return humidity
s1=Sensor('hom/parking/thermoset/ggd',pin=100)
print(s1.read_sensor_type())
       
d1=Device('hom / parking / laps / lamps138')
d1.topic
my_list=d1.topic_list
d1.location
d1.device_typ
d1.name


