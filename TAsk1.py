'''

APM:


Salam daryaft shod




'''



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

#****************************************
class Device:
    def __init__(self,topic): 
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_typ=self.topic_list[2]
        self.device_name =self.topic_list[3]
        self.status='off'

    def turn_on(self):
        self.status='on'
        print('turn_on')

    def turn_off(self):
        self.status='off'
        print('turn off')
    def get_status(self):
        print(f'your device is : {self.status}')
     # in def halat koli device ro nshoon mide
class Sensor:
    def __init__(self,topic):
      self.topic=topic
      self.topic_list=self.topic.split('/')
      self.location=self.topic_list[0]
      self.groups=self.topic_list[1]
      self.snsor_typ=self.topic_list[2]
      self.sensor_name =self.topic_list[3]   
    def read_sensor(self):
        return 25 
class Admin_panel:
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[] 
            print(f'group_name {group_name} created')
        else:
            print('your group name is exist alredy')
    def add_device_to_group(self,group_name,devaice):
        if group_name in self.groups:
            self.groups[group_name].append(devaice)
            print(f'device_name is added to ,{group_name}')
            #*******task2
        else:
            print(f'group{group_name}is not exist')
    def creat_device(self,group_name,device_typ,name):
        if group_name in self.groups:
            topic=f'hom/{group_name}/{device_typ}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name,new_device)
        #********task2
        
            print(f'{new_device} add to {self.groups}')
        else:
            print(f'group{group_name}is not exist')
    def create_multiple_device(self,group_name,device_type,number_of_device):
         if group_name in self.groups:
             for i in range(1,number_of_device+1):
                 topic=f'hom/{group_name},{device_type},{device_type}{i}'
                 new_device=Device(topic)
                 self.add_device_to_group(group_name, new_device)
                 #************task 2
                 print(f'{group_name},{device_type},{device_type}{i}')             
         else:
            print(f'group{group_name}is not exist')
               
    def turn_on_device_in_group(self,group_name):
        if group_name in self.groups:
            device_list=self.groups[group_name]
            for device in device_list:
                device.turn_on()
        else:
            print(f'group{group_name}is not exist')
#task 3
    def turn_off_device_in_group(self,group_name):
      if group_name in self.groups:
          device_list=self.groups[group_name]
          for device in device_list:
              device.turn_off()
      else:
          print(f'group{group_name}is not exist')
      def turn_on_all_device(self):
           for group_name in self.groups:
               for device in self.groups[group_name]:
                   device.turn_on()

      def get_status_in_group(self, device_type):
           for group_name, devices in self.groups.items():
               print(f"Status of {device_type} devices in group {group_name}:")
               for device in devices:
                   if device.device_type == device_type:
                       device.get_status()

      def get_status_in_device_type(self, device_type):
           print(f"Status of all {device_type} devices:")
           for group_name, devices in self.groups.items():
               for device in devices:
                   if device.device_type == device_type:
                       device.get_status()

      def get_status_sensor_in_group(self, group_name):
           if group_name in self.groups:
               print(f"Sensor readings for group {group_name}:")
               for item in self.groups[group_name]:
                   if isinstance(item, Sensor):
                     reading = item.read_sensor()
                     print(f"  {item.sensor_name}: {reading}")
                   else:
                     print(f"There is no sensor in the {group_name}")
           else:
               print(f'Group {group_name} does not exist')
        
 
       
a=Admin_panel()
#ta inja omad ye dicshenery khali dorost kard
#halamiam ba def creat too dic list ba nam delkhoh misazim
a.create_group('parking')
a.create_group('WC')
a.create_group('room1')
a.create_group('kichen')
mydevice=Device(topic='hom/kichen/lams/lamp123')
a.add_device_to_group('parking', mydevice)
a.groups
a.creat_device('WC', 'lamps', 'lams12')
a.groups
mygp=a.groups
print(type(mygp))
mygp.keys()
mygp.values()
a.create_multiple_device('parking', 'lamps', 40)
mygp=a.groups
for group in mygp:
    for divice in mygp[group]:
        print(device.devaice_name)# دقیقه 45.27
