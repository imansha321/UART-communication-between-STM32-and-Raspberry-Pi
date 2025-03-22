import serial

ser = serial.Serial('/dev/serial0', baudrate=115200, timeout=1)
data_str = ""

try:
    while True:
        if ser.in_waiting > 0:  
            data = ser.read(1)  
            data_str += str(data.decode('utf-8'))
            if str(data.decode('utf-8')) == "\n":
                print(data_str)
                data_str = ""
       
        
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()

