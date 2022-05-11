# Misc / Color plant 2

## Challenge :star::star:
> Dans cette deuxième partie du challenge Color Plant, votre objectif sera de manipuler l'usine en production afin de remplir une cuve avec la couleur RGB(32, 126, 42) et ce dans un temps limité à 90 secondes. Pour cela, vous devrez ouvrir et fermer des vannes au bon moment, ajuster des débits en manipulant les différents registres de l'automate via le protocole Modbus.

## Inputs
- Description of how the color plant works `https://france-cybersecurity-challenge.fr/pheidee8ooPee3eghoo3ooh3sae0ooLo`
- Entry point to the color plant `challenges.france-cybersecurity-challenge.fr:502`
- SCADA Web interface for the plant `https://color-plant.france-cybersecurity-challenge.fr`

## Solution
This is 2nd part of the color plant challenge.
First part was about reading a token from some Modbus registers to access the web api.

Here we need to fill tank F with `RGB(32,126,42)` in less than 90s.
Now, tank F has a capacity of 200 units of color, but above tank M only has a capacity of 100 units.
So we have to fill tank M twice with `RGB(16,63,41)`.

To easier things, I decided to fill the tank M with each color one after the other.
I wasn't sure it would work because of the time limit, but it did!

So overall we want to do this twice:
- Open tank R and adjust the throughput (we'll come to that next)
- Read tank M for the number of R units, until the target R=16 is reached, then close tank R.
- Same for tank G (target G=63)
- Same for tank B (target B=41)
- At this point, tank M is filled with `RGB(16,63,41)` and tanks RGB are closed
- Open tank F and adjust the throughput
- Read tank F for total quantity, until the target=0 is reached, then close tank F (shouldn't be necessary because of the safety program)

To implement this, I need to read/write all registers, using these API calls:
```python
c.read_coils(coil, 1)
c.write_single_coil(coil, val)
c.read_holding_registers(hreg, 1)
c.read_input_registers(inreg, 1)[0]
c.write_single_register(reg, val)
```

Then I define some abstraction layer above those, to easier the implementation:
```python
status_cuve_R()
status_cuve_G()
status_cuve_B()
open_cuve_R()
open_cuve_G()
open_cuve_B()
close_cuve_R()
close_cuve_G()
close_cuve_B()
open_cuve_final()
close_cuve_mix()
read_debit_R()
read_debit_G()
read_debit_B()
write_debit_R(debit)
write_debit_G(debit)
write_debit_B(debit)
read_debit_mix()
write_debit_mix(debit)
read_cuve_R()
read_cuve_G()
read_cuve_B()
read_mix_R()
read_mix_G()
read_mix_B()
read_mix_total()
read_final_R()
read_final_G()
read_final_B()
read_final_total()
```

About the throughput control, as far as I remember from my experiments:
- max is 5 units per second
- going too fast and you may miss your target (like when your target 16 units of R in tank M)
- going too slowly and you may not do it in the time limit!

So my strategy about throughput control was to use max throughput (T) of 5u/s up to a bit less that the target.
Then to use min throughput (T) of 1u/s up to the target.
- R: T=4 allows to reach 16u in one step
- G: T=5 up to 60u, then T=1 slowly to reach 63u
- B: T=5 up to 20u, then T=1 slowly to reach 21u

Last piece is some function to read the R/G/B quantities in tank M in a loop.
Until some target is reached, and tank can be closed.
```python
close_cuve_R_on_quantity(q)
close_cuve_G_on_quantity(q)
close_cuve_B_on_quantity(q)
close_cuve_mix_on_quantity(q)
```

To wrap up, here is the full sequence to fill tank F with `RGB(16,63,21)`, called twice:
```python
def scada():
    close_cuve_R()
    close_cuve_G()
    close_cuve_B()
    # R: open & adjust rate: T=4 allows to reach 16u in one step.
    write_debit_R(4)
    open_cuve_R()
    close_cuve_R_on_quantity(16)
    # G: open & adjust rate: T=5 up to 60u, then T=1 slowly to reach 63u
    write_debit_G(5)
    open_cuve_G()
    close_cuve_G_on_quantity(60)
    #status_M()
    write_debit_G(1)
    open_cuve_G()
    close_cuve_G_on_quantity(63)
    # B: open & adjust rate: T=5 up to 20u, then T=1 slowy to reach 21u
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
```

With this, we can fill tank F as specified, with ~20s time left.
The flag is then displayed in the events log.

Very nice challenge. The animation in the web api is pretty slick.

## Python code
Complete solution in [sol.py](sol.py)

## Flag
FCSC{3518dcd9579b4f2bf4ab32f126aa746e00767d6b130ef6c2e79ae6a313d0ba07}
