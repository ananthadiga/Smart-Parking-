# Smart-Parking-
Smark Parking is a IOT project, the project Helps us to automate parking. 
With the advancement in technology cities have become smarter. Take an example of smart traffic management or smart water treatment have changed the way cities work. One of the aspects where technology can be used to make cities smart is parking. Parking facilities has become a huge problem nowadays.This problem is due to unplanned housings that has increased the number of vehicles. This leads to creating mess everywhere and also increases traffic. This kind of problem mainly arises in street(open) parking. There is a need of an application that could let the people know where to park their vehicles before hand to avoid the traffic congestion An estimation of 3 million vehicles on roads in major cities across globe.
Objective
Since there is an increasing number of vehicles, there has to be sufficient number of parking spaces made available.
In this project, entire focus is put upon parking spaces in closed areas(shopping malls).
This project is designed in such a way that energy, time and fuel are conserved.
We built a model which is a replica of a mall we used IOT & Embedded System in the project to solve parking issue. We automated 90% of the work. We stored data in the cloud & used php as our script language.
Working of the project in General

When a car enters into the parking lot, the LCD screen displays the information as to where the car should go and park.
This information to the LCD is given by sensors that are placed, in each parking lot.
When there is no car parked, the LED glows green, and no light glows when the slot is occupied.
When the slot is full, the sensors send information to the display and the database, where the data is stored in the database.
This data is displayed on the web screen and will be saved in it until we rerun the program.

Building our Model
First we started with writing a python code for measuring distance between objects using ultra-sonic sensor. We also tried to measure distance using IR sensor but when compared to ultra-sonic the effectiveness was lower. So we went on with ultra-sonic
We placed ultra-sonic sensor in each of the slots. We had eight slots so a total of 8 sensors were used. The entire ultra-sonic sensor is connected to Raspberry Pi and gave a real time measurement. We used 15 CMS as default distance if the distance is less than 15, display slots is not empty & if the distance is more than 15 centimetres, display slots are not empty.
LED is used as indicator, if the distance is less than 15 blink the LED an indicator of slots being occupied. 
We used a LCD to display the info about which slots are empty; it is placed in the beginning so that the driver entering will have an idea where to park. We also had a motor which rotates when at least one of the slots are free acting as a gate. 

All the info from sensors are inter-linked LCD, LED & Ultra-Sonic Sensors.
And all the data is stored on the local disk & it works in real time.
This is how our model looks 


Code for ultrasonic sensor 
if distance > 15:
        print " slot 2 is empty"
     
        lcd.message('slot2 is empty')
    else :
        print"slot 2 is not empty"
      
If the value is less than 15, print slot is empty and lcd will display slot 2 is empty.
Website Building
We used Apache to build local host & php as a scripting language. The data from the local server is transferred to MySql using python program & we used php, PhpMyAdmin to display the real time information. The eight slots information was displayed on the website. This information can be accessed be device before coming to the mall. We wanted to add feature of booking the slot but unfortunately it isn’t implemented.
We used MySql connect to transfer data from the photon code to the MySql Database. 
Code for using MySql Connect.
db = MySQLdb.connect("localhost","root","root","smart" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS SMARTP")
sql = """CREATE TABLE SMARTP (
         slot_number INT  ,
         status  CHAR(20) ) """
         #PRIMARY KEY (slot_number) ) """

cursor.execute(sql)

cursor = db.cursor()

