# Hardware / Qui est-ce ?

## Challenge :star::star:
> On vous donne le circuit logique en pièce jointe, et on vous demande de donner une entrée sous forme décimale correspondante à la sortie y = 8549048879922979409, avec yi les bits de y où y62 est le MSB et y0 le LSB : (y62, ..., y0) = (1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1).
>Encadrez votre réponse entre FCSC{} pour obtenir le flag.

    Exemple : si on avait donné y = 1333333333333333337, alors le flag aurait été FCSC{6497282320360345885}.

## Input
- A PDF file showing a circuit  [circuit](circuit.pdf)

## Solution
Let's use `z3` SMT solver to solve the circuit ant get back to input `[x62..x0]` from provided output `[y62..y0]`. First time I'm using `z3` there, so the way I'm using it is probably suboptimal.

Revert the output to get `y62..y0`, i.e. `y0=LSB` and `y62=MSB`. We know `y0..y62`.
```python
y = y__[::-1]
```

Declare the collection of input variables `x0..x62`. I assume there's a way to declare a list of those, but oh well..
```python
x0 = Bool('x0')
..
x62 = Bool('x62')
```

Create the SMT solver instance. Add the constraints giving output `y0..y62` as a (Boolean) expression of input `x0..x62`.
```python
s = Solver()
s.add(
Xor(x0,  And(x61, Not(x62))) == y[0],
..
Xor(x62, And(x60, Not(x61))) == y[62],
)
```

Retrieve the inputs `xO..x62` from the solver solution. Again, using a list would make it so much better...
```python
sol[0] = m[x0]
..
sol[62] = m[x62]
```

Finally revert and get the input as a decimal: 7364529468137835333.

## Python code
Solution in [sol.py](sol.py)

## Flag
FCSC{7364529468137835333}
