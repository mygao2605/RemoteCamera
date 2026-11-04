import json
            
class Config:
    with open("app_config.json", "r", encoding="utf-8") as f:
        app_config = json.load(f)
    
    SLAVE_ID = app_config["SLAVE_ID"]
    SERIAL_PORT = app_config["SERIAL_PORT"]
    BAUDRATE = app_config["BAUDRATE"]
    IP = app_config["IP"]
    PORT = app_config["PORT"]
