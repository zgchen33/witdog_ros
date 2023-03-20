import serial
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=1000000, bytesize=serial.EIGHTBITS, timeout=0)
ser.flush()
