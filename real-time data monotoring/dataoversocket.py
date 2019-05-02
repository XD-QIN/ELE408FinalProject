from sense_hat import *
from time import sleep
import pygal
import socket
import subprocess

temp = []
sense = SenseHat()
weather= pygal.Line()
i =0;
host = '192.168.1.103'
port = 5000

s = socket.socket()
s.connect((host,port))
while (True):
    sleep(1)
    myfile = open('weather.txt','a')
    temp.append(sense.temp)
    high_temp = sense.temp
    cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
    array = cpu_temp.split("=")
    array2 = array[1].split("'")
    cpu_tempf = float(array2[0])
    calibrated_temp = sense.temp - ((cpu_tempf - high_temp)*0.75)
    yourstring = str(sense.temp)
    alldatastring = str(i) + ' ' + str(calibrated_temp) + ' ' + str(sense.pressure) + ' ' + str(sense.humidity)  
    print(alldatastring)
    s.sendto(alldatastring.encode('utf-8'),(host,port))
    weather.add('temp',temp)
##    weather.render_to_file('/home/pi/osoyoo-robot/cam_robot/robot/temp_history.svg')
##    myfile.write(str(sense.temp))
##    myfile.write('\n')
##    myfile.close()
    i=i+1
    
weather.render()    
weather.render_to_file('temp_history.svg')

s.close()
