# all imports
import time
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.rect import Rect
import board
import displayio
import socketpool
import ssl
import adafruit_requests
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_display_text import label
import terminalio  # Built-in font
import wifi
import os
import math

#==CODE_STARTS_HERE==#

# Opens and reads from the city text file
try:
    with open("/city.txt", "r") as file:
        city = file.read().strip()
except OSError:
    city = "Liverpool" # Where it was Created (Decided to change from Manchester on 27/06/2025)

pool = socketpool.SocketPool(wifi.radio) #Initialises low level networking support
requests = adafruit_requests.Session(pool, ssl.create_default_context()) # Sets up a HTTP Client which can make secure API requests 

# Initialize MatrixPortal
matrixportal = MatrixPortal(
    status_neopixel=board.NEOPIXEL,
    debug=True,
    height=64,
    width=64,
    bit_depth=2
)

# Collects the Information from Setting.toml and connects to mobile hotspot
wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
api_key = os.getenv("OPENWEATHER_API_KEY")

# Collects the Requested Weather Information from here
def get_Weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# any time this variable is used it calls the function
weather = get_Weather()

# Checks to See if the Name of the City is Valid, and displays an Error message if it isnt
if weather is None:
    display = matrixportal.graphics.display
    main_group = displayio.Group()

    ECode = label.Label(terminalio.FONT, text=f"ERROR 404", color=0xF0F0FF, x=5, y=22)
    EMessage = label.Label(terminalio.FONT, text=f"TRY AGAIN!", color=0xF0F0FF, x=3, y=32)
    bob = label.Label(terminalio.FONT, text=f"NEW NAME!", color=0xF0F0FF, x=6, y=42)
    main_group.append(ECode)  
    main_group.append(EMessage)  
    main_group.append(bob)

    display.root_group = main_group
    while True:
        pass  # halt here


j = True # i honestly dont know why but it works
while (j == True):
    # because the output from the API is a nested python object, you need to do into each object (Think steps or a mind map)
    nameResult = weather["name"]
    temperatureResult = weather["main"]["temp"] 
    j = False

# Rounds it up
if isinstance(temperatureResult, float):
        temperatureResult = math.floor(temperatureResult)

display = matrixportal.graphics.display

# Create the main display group
main_group = displayio.Group()


if (temperatureResult > 30):
     heat = 0XFF0000 #RED

elif (temperatureResult > 25 and temperatureResult < 30):
     heat = 0XFFA500 #YELLOW

elif (temperatureResult < 25 and temperatureResult > 10):
     heat = 0x008000 #GREEN

elif (temperatureResult <10):
     heat = 0X0000FF #BLUE


Sky = Rect(x=0, y=0, width=64, height=64, fill=0x001060)

circle = Circle(31, 31, 20, fill=0x8B5E00, outline=0x8B5E00)

place = label.Label(terminalio.FONT, text=str(nameResult), color=0X000000,  x=3, y=25, scale=1)
place_outline = label.Label(terminalio.FONT, text=str(nameResult), color=0XFFFFFF,  x=2, y=24, scale=1)

temperature = label.Label(terminalio.FONT, text=f"Temp={temperatureResult}C", color=0X000000, x=9, y=36)
temperature_outline = label.Label(terminalio.FONT, text=f"Temp={temperatureResult}C", color=0xFFFFFF, x=8, y=35)

main_group.append(Sky)
main_group.append(circle)
#main_group.append(place2)
main_group.append(place)
main_group.append(place_outline)
main_group.append(temperature)
main_group.append(temperature_outline)


# Show everything
display.root_group = main_group

while True:
    time.sleep(1)   

#192.168.le
# init display au

# 11 bottom
# 12 top