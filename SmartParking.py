import RPi.GPIO as GPIO                    #Import GPIO library
import time
import Adafruit_CharLCD as LCD
import MySQLdb
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
GPIO.setwarnings(False)
TRIG1 = 20                                  #Associate pin 23 to TRIG
ECHO1 = 21
TRIG2 = 12                                 #Associate pin 23 to TRIG
ECHO2 = 16
TRIG3 = 23
ECHO3 = 24
TRIG4 = 27
ECHO4 = 22
TRIG5 = 4
ECHO5 = 17
print "Distance measurement in progress"
lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 06
lcd_d6 = 05
lcd_d7 = 11
lcd_backlight = 2
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
GPIO.setup(TRIG1,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(TRIG4,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO4,GPIO.IN)
GPIO.setup(TRIG5,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO5,GPIO.IN)


db = MySQLdb.connect("localhost","root","root","smart" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS SMARTP")
sql = """CREATE TABLE SMARTP (
         slot_number INT  ,
         status  CHAR(20) ) """
         #PRIMARY KEY (slot_number) ) """

cursor.execute(sql)


cursor = db.cursor()




def slot1():
    GPIO.output(TRIG1, False)                 #Set TRIG as LOW
 # print "Waitng For Sensor To Settle"
    time.sleep(2)                           #Delay of 2 seconds
    GPIO.output(TRIG1, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG1, False)                 #Set TRIG as LOW
    while GPIO.input(ECHO1)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO1)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    distance = pulse_duration * 17150        #Multiplyexuse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points


    if distance > 20:
        print " slot 1 is empty"
        x1="slot 1 is empty"
        lcd.message('slot1 is empty')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
    else :
        print"slot 1 is not empty"
        x1=" "
    return x1

p = slot1()

    #print "Out Of Range"                   #display out of range

def slot2():
    GPIO.output(TRIG2, False)                 #Set TRIG as LOW
 # print "Waitng For Sensor To Settle"
    time.sleep(2)
    lcd.clear()                                 #Delay of 2 seconds
    GPIO.output(TRIG2, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG2, False)                 #Set TRIG as LOW
    while GPIO.input(ECHO2)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO2)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    distance = pulse_duration * 17150        #Multiplyexuse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points


    if distance > 20:
        print " slot 2 is empty"
        x2="slot 2 is empty"
        lcd.message('slot2 is empty')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    else :
        print"slot 2 is not empty"
        x2=" "
    return x2
y = slot2()

def slot3():
    GPIO.output(TRIG3, False)                 #Set TRIG as LOW
     # print "Waitng For Sensor To Settle"
    time.sleep(2)
    lcd.clear()                                 #Delay of 2 seconds
    GPIO.output(TRIG3, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG3, False)                 #Set TRIG as LOW
    while GPIO.input(ECHO3)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO3)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    distance = pulse_duration * 17150        #Multiplyexuse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points



    if distance > 20:
        print " slot 3 is empty"
        x3="slot 3 is empty"
        lcd.message('slot3 is empty')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    else :
        print"slot 3 is not empty"
        x3=" "
    return x3

z = slot3()

def slot4():
    GPIO.output(TRIG4, False)                 #Set TRIG as LOW
 # print "Waitng For Sensor To Settle"
    time.sleep(2)
    lcd.clear()                                 #Delay of 2 seconds
    GPIO.output(TRIG4, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG4, False)                 #Set TRIG as LOW
    while GPIO.input(ECHO4)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO4)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    distance = pulse_duration * 17150        #Multiplyexuse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points
    
    if distance>20:
        print " slot 4 is empty"
        x4='slot 4 is empty'
        lcd.message('slot4 is empty')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    else:
        print " slot 4 is not empty"
        x4=" "
    return x4
s = slot4()

def slot5():
    GPIO.output(TRIG5, False)                 #Set TRIG as LOW
 # print "Waitng For Sensor To Settle"
    time.sleep(2)
    lcd.clear()                                 #Delay of 2 seconds
    GPIO.output(TRIG5, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG5, False)                 #Set TRIG as LOW
    while GPIO.input(ECHO5)==0:               #Check whether the ECHO is LOW
        pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO5)==1:               #Check whether the ECHO is HIGH
        pulse_end = time.time()                #Saves the last known time of HIGH pulse 

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
    distance = pulse_duration * 17150        #Multiplyexuse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points
    
    if distance>20:
        print " slot 5 is empty"
        x5= 'slot 5 is empty'
        lcd.message('slot5 is empty')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
    
    else:
        print "slot 5 is not empty"
        x5=" "
    return x5
t=slot5()
a = 'slot 1 is empty'
b = 'slot 2 is empty'
c = 'slot 3 is empty'
d = 'slot 4 is empty'
e = 'slot 5 is empty'

while True:
    slot1()
    if p == a:
        print "go to slot 1"
        
        sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (1,'emptY')"""
        try:
        	cursor.execute(sql)
        	db.commit()
        except:
        	db.rollback()
    slot2()
    if y == b:
        print "go to slot 2"
        
        sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (2,'empty')"""
        try:
                cursor.execute(sql)
                db.commit()
        except:
                db.rollback()
    slot3()
    if z == c:
        print "go to slot 3"
        
        sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (3,'empty')"""
        try:
                cursor.execute(sql)
                db.commit()
        except:
                db.rollback()
    slot4()
    if s == d:
        print "go to slot 4"
        
        sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (4,'empty')"""
        try:
                cursor.execute(sql)
                db.commit()
        except:
                db.rollback()
    slot5()
    if t == e:
        print "go to slot 5"
        
        sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (5,'empty')"""
        try:
         	cursor.execute(sql)
                db.commit()
        except:
                db.rollback()
   
    
    sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (6,' non empty')"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    

    
    sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (7,' non empty')"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()




 
    sql = """INSERT INTO SMARTP(slot_number,
            Status)
            VALUES (8,' non empty')"""
    try:
    	cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

   

db.close()

