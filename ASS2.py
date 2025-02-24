from machine import Pin, ADC
import ujson
import network
import utime as time
import dht
import urequests as requests
from time import sleep

# Device di Ubidots
DEVICE_ID = "esp32_rpp"
TOKEN = "BBUS-RPfpW6yvrKdsnHifNK81PNNzFd6rxV"

# MongoDB API
MONGO_API = "http://192.168.251.119:5000/sensor"

# Pin
DHT_PIN = Pin(18)
PIR_PIN = Pin(23, Pin.IN)
led =Pin(22,Pin.OUT)

# Cara connect Hotspot
def do_connect():
    import network
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        print("Connecting to network")
        sta_if.active(True)
        sta_if.connect('Samsung A55', '18072005')
        while not sta_if.isconnected():
            pass
        print('network config:', sta_if.ipconfig('addr4'))

# Cara connect Wifi
def do_connect1():
    wifi_client = network.WLAN(network.STA_IF)  
    wifi_client.active(True)
    print("Connecting device to WiFi")
    wifi_client.connect("R_MB317A_5G", "gakmaukasihtau")

    while not wifi_client.isconnected():
        print("Connecting")
        time.sleep(0.1)
    print("WiFi Connected!")
    print(wifi_client.ifconfig())

def did_receive_callback(topic, message):
    print('\n\nData Received! \ntopic = {0}, message = {1}'.format(topic, message))

def create_json_data(temperature, humidity, motion, led_state):
    data = ujson.dumps({
        "device_id": DEVICE_ID,
        "temp": temperature,
        "humidity": humidity,
        "motion": motion,
        "led": led_state,
        "type": "sensor"
    })
    return data

# Send data
def send_data(temperature, humidity, motion, led_state):
    url = "http://industrial.api.ubidots.com/api/v1.6/devices/" + DEVICE_ID
    headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
    data = {
        "temp": temperature,
        "humidity": humidity,
        "motion": motion,
        "led": led_state
    }
    
    response = requests.post(url, json=data, headers=headers)
    print("Done Sending Data!")
    print("Response:", response.text)

def send_data2(temperature, humidity, motion, led_state):
    
    headers = {"Content-Type": "application/json"}
    data = {
        "device_id": DEVICE_ID,
        "temperature": temperature,
        "humidity": humidity,
        "motion": motion,
        "led": led_state,
        "timestamp": time.time()  # Tambahkan timestamp
    }
    
    try:
        response = requests.post(MONGO_API, json=data, headers=headers)
        print("Done Sending Data to MongoDB!")
#         print("MongoDB Response:", response.text)
    except Exception as e:
        print("Error sending data to MongoDB:", str(e))

do_connect();

dht_sensor = dht.DHT11(DHT_PIN)
telemetry_data_old = ""

# Declare nilai awal
motion = 0
led_state = 0

# Tes
while True:
    try:
        dht_sensor.measure()
        motion = PIR_PIN.value()
        if motion == 1:
            led.value(1)
            led_state = 1
        else:
            led.value(0)
            led_state = 0

    except:
        pass

    time.sleep(0.5)
    telemetry_data_new = create_json_data(dht_sensor.temperature(), dht_sensor.humidity(), motion, led_state)
    send_data(dht_sensor.temperature(), dht_sensor.humidity(), motion, led_state)
    send_data2(dht_sensor.temperature(), dht_sensor.humidity(), motion, led_state)
    time.sleep(0.5)


