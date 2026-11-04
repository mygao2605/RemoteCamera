from flask import Flask
from pymodbus.client import ModbusSerialClient
from config import Config
app = Flask(__name__)


client = ModbusSerialClient(
    port=Config.SERIAL_PORT,
    baudrate=Config.BAUDRATE,
    parity='E',
    stopbits=1,
    bytesize=8,
    timeout=1
)

if not client.connect():
    print("Cannot connect Modbus")
    exit()

print("Modbus Connected")


def send_command(cmd):
    start = 1
    speed = 3000
    left  = 0
    right = 0
    up    = 0
    down  = 0
    if cmd == "left":
        left = 1
    elif cmd == "right":
        right = 1
    elif cmd == "up":
        up = 1
    elif cmd == "down":
        down = 1
    elif cmd == "stop":
        start = 1
        speed = 3000
        left  = 0
        right = 0
        up    = 0
        down  = 0
    else:
        start = 1
        speed = 0
        left  = 0
        right = 0
        up    = 0
        down  = 0

    data = [
        start,     # Reg0
        speed,     # Reg1
        left,      # Reg2
        right,     # Reg3
        up,        # Reg4
        down       # Reg5
    ]

    print("SEND:", cmd)
    print("MODBUS:", data)

    result = client.write_registers(
        address=0,
        values=data,
        device_id=Config.SLAVE_ID
    )

    if result.isError():
        return "Write Error"


@app.route('/cmd=<cmd>')
def command(cmd):

    response = send_command(cmd)

    return response


app.run(
    host=Config.IP,
    port=Config.PORT,
    debug=False
)