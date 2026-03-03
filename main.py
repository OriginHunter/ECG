import serial

ser = serial.Serial('COM3', 115200)
raw_data: bytes = ser.read(9)
data = raw_data.decode('utf-8')
print(f"读取10字节数据：{raw_data}，转换为字符串：{data:}")
