from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)

if client.connect():
    print("modbus conectado")
else:
    print("modbus no conectado")

k = 0


while k < 700:
    
    client.write_coil(address=18, value=True, device_id=1)
    
    on = client.read_discrete_inputs(address=20, count=1, device_id=1)
    onBit = on.bits[0]
    
    print(onBit)
    
    k += 1

client.close()