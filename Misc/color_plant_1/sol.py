from pyModbusTCP.client import ModbusClient
import time

# Connect to port 502
c = ModbusClient(host="challenges.france-cybersecurity-challenge.fr", port=502, auto_open=True)

# Read 32 'Holding' registers starting at address 0 to get the token
# Return it as a string
def read_token():
    token = c.read_holding_registers(0, 32)
    s = s_ = ""
    for i in range(len(token)):
        s = s + chr(token[i])
    print(s)
    return s


token = read_token()
time.sleep(60)

# FCSC{266350f412840c932b29bb095394d318c17c844f70c05f49c9998a8e614be531}
