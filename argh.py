def argh(code):
    (pointer := [0,0])
    (direction := [0])
    (stack := [])
    (field := [list(l)+[" "]*(80-len(l)) for l in code.split("\n")]+[["  "]*80]*(40-len(code.split("\n"))))
    while 1:
        {
            "A":lambda: stack.__setitem__(-1, stack[-1]+ord(field[pointer[0]-1][pointer[1]])),
            "a":lambda: stack.__setitem__(-1, stack[-1]+ord(field[pointer[0]+1][pointer[1]])),
            "D":lambda: stack.pop(),
            "d":lambda: stack.append(stack[-1]),
            "E":lambda: field[pointer[0]-1].__setitem__(pointer[1], chr(26)),# I was told that 26 is the char code for EOF
            "e":lambda: field[pointer[0]+1].__setitem__(pointer[1], chr(26)),
            "F":lambda: field[pointer[0]-1].__setitem__(pointer[1], chr(stack.pop())),
            "f":lambda: field[pointer[0]+1].__setitem__(pointer[1], chr(stack.pop())),
            "G":lambda: field[pointer[0]-1].__setitem__(pointer[1], input()[0]),# TODO: CTRL+D = EOF
            "g":lambda: field[pointer[0]+1].__setitem__(pointer[1], input()[0]),
            "H":lambda: [pointer.__setitem__(1, pointer[1]-list(reversed(field[pointer[0]][0:pointer[1]])).index(chr(stack[-1]))),direction.__setitem__(0, 2)],
            "h":lambda: direction.__setitem__(0, 2),
            "J":lambda: [pointer.__setitem__(0, pointer[0]+[l[0] for l in field[pointer[0]:]].index(chr(stack[-1]))), direction.__setitem__(0, 1)],
            "j":lambda: direction.__setitem__(0, 1),
            "K":lambda: [pointer.__setitem__(0, pointer[0]-list(reversed([l[0] for l in field[0:pointer[0]]])).index(chr(stack[-1]))), direction.__setitem__(0, 3)],
            "k":lambda: direction.__setitem__(0, 3),
            "L":lambda: [pointer.__setitem__(1, pointer[1]-field[pointer[0]][pointer[1]:].index(chr(stack[-1]))),direction.__setitem__(0, 0)],
            "l":lambda: direction.__setitem__(0, 0),
            "P":lambda: print(end=field[pointer[0]-1][pointer[1]]),
            "p":lambda: print(end=field[pointer[0]+1][pointer[1]]),
            "q":lambda: exit(),
            "R":lambda: stack.__setitem__(-1, stack[-1]-ord(field[pointer[0]-1][pointer[1]])),
            "r":lambda: stack.__setitem__(-1, stack[-1]-ord(field[pointer[0]+1][pointer[1]])),
            "S":lambda: stack.append(ord(field[pointer[0]-1][pointer[1]])),
            "s":lambda: stack.append(ord(field[pointer[0]+1][pointer[1]])),
            "X":lambda: direction.__setitem__(0, (direction[0]+3)%4) if stack[-1]<0 else None,
            "x":lambda: direction.__setitem__(0, (direction[0]+1)%4) if stack[-1]<0 else None,
            "#":lambda: direction.__setitem__(0, 1) if pointer==[0,0] and field[0, 1] == "!" else None
        }.get(field[pointer[0]][pointer[1]], lambda: [print("[ARGH!]"), exit()])()
        {
            0: lambda: pointer.__setitem__(1, pointer[1]+1),
            1: lambda: pointer.__setitem__(0, pointer[0]+1),
            2: lambda: pointer.__setitem__(1, pointer[1]-1),
            3: lambda: pointer.__setitem__(0, pointer[0]-1)
        }[direction[0]]()

argh('''j       world
lppppppPPPPPPsrfj
 hello,      *  j
              qPh''')