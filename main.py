# TEST CONNECTION

from pyModbusTCP.client import ModbusClient
from time import sleep

WAGO_IP = '192.168.0.24'
MODBUS_PORT = 502
COIL_ON = True
COIL_OFF = False

client = ModbusClient(host=WAGO_IP, port=MODBUS_PORT)


def coil_on():
    for coil_nr in range(0, 11):
        client.write_single_coil(coil_nr, COIL_ON)
        sleep(1)


def coil_off():
    for coil_nr in range(0, 11):
        client.write_single_coil(coil_nr, COIL_OFF)
        sleep(1)


def coil_read():
    print(client.read_coils(0, 10))


if __name__ == '__main__':
    coil_on()
    coil_read()
    sleep(5)
    coil_off()
    coil_read()
