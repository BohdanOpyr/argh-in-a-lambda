def argh(code):
    (ptr := [0,0])
    (direction := [0])
    (sck := [])
    (field := [list(l)+[" "]*(80-len(l)) for l in code.split("\n")]+[["  "]*80]*(40-len(code.split("\n"))))
    (ss:=sck.__setitem__)
    (setx:=lambda a:ptr.__setitem__(1, a))
    (sety:=lambda a:ptr.__setitem__(0, a))
    while 1:# TODO:CTRL+D = EOF
        {"A":lambda:ss(-1,sck[-1]+ord(field[ptr[0]-1][ptr[1]])),"a":lambda:ss(-1,sck[-1]+ord(field[ptr[0]+1][ptr[1]])),"D":lambda:sck.pop(),"d":lambda:sck.append(sck[-1]),"E":lambda:field[ptr[0]-1].__setitem__(ptr[1],chr(26)),"e":lambda:field[ptr[0]+1].__setitem__(ptr[1],chr(26)),"F":lambda:field[ptr[0]-1].__setitem__(ptr[1],chr(sck.pop())),"f":lambda:field[ptr[0]+1].__setitem__(ptr[1],chr(sck.pop())),"G":lambda:field[ptr[0]-1].__setitem__(ptr[1],input()[0]),"g":lambda:field[ptr[0]+1].__setitem__(ptr[1],input()[0]),"H":lambda:[ptr.__setitem__(1,ptr[1]-list(reversed(field[ptr[0]][0:ptr[1]])).index(chr(sck[-1]))),direction.__setitem__(0,2)],"h":lambda:direction.__setitem__(0,2),"J":lambda:[sety(ptr[0]+[l[0] for l in field[ptr[0]:]].index(chr(sck[-1]))),direction.__setitem__(0,1)],"j":lambda:direction.__setitem__(0,1),"K":lambda:[sety(ptr[0]-list(reversed([l[0] for l in field[0:ptr[0]]])).index(chr(sck[-1]))),direction.__setitem__(0,3)],"k":lambda:direction.__setitem__(0,3),"L":lambda:[ptr.__setitem__(1,ptr[1]-field[ptr[0]][ptr[1]:].index(chr(sck[-1]))),direction.__setitem__(0,0)],"l":lambda:direction.__setitem__(0,0),"P":lambda:print(end=field[ptr[0]-1][ptr[1]]),"p":lambda:print(end=field[ptr[0]+1][ptr[1]]),"q":lambda:exit(),"R":lambda:ss(-1,sck[-1]-ord(field[ptr[0]-1][ptr[1]])),"r":lambda:ss(-1,sck[-1]-ord(field[ptr[0]+1][ptr[1]])),"S":lambda:sck.append(ord(field[ptr[0]-1][ptr[1]])),"s":lambda:sck.append(ord(field[ptr[0]+1][ptr[1]])),"X":lambda:direction.__setitem__(0,(direction[0]+3)%4) if sck[-1]<0 else None,"x":lambda:direction.__setitem__(0,(direction[0]+1)%4) if sck[-1]<0 else None,"#":lambda:direction.__setitem__(0,1) if ptr==[0,0] and field[0,1] == "!" else None}.get(field[ptr[0]][ptr[1]],lambda:[print("[ARGH!]"),exit()])()
        [lambda:setx(ptr[1]+1),lambda:sety(ptr[0]+1),lambda:setx(ptr[1]-1),lambda:sety(ptr[0]-1)][direction[0]]()

argh('''j       world
lppppppPPPPPPsrfj
 hello,      *  j
              qPh''')