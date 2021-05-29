t = lambda t, f=lambda a:a, e=Exception,:(r:={}).pop(
    'r',
    type(
        '',
        (__import__('contextlib').ContextDecorator,),
        {
            '__enter__':int,
            '__exit__':lambda s,*a:isinstance(
                a[1], e
            ) and [r.update(
                r=f(a)
            )]
        }
    )()(t)()
)# Inline error handling, credit: chilaxan from python discord; modified version
def argh(c):
    (p := [0,0])
    (r := [0])
    (k := [])
    (field := [list(l)+[" "]*(80-len(l)) for l in c.split("\n")]+[["  "]*80]*(40-len(c.split("\n"))))
    (s:=k.__setitem__)
    (x:=lambda a:p.__setitem__(1,a))
    (y:=lambda a:p.__setitem__(0,a))
    list(iter(lambda: [{"A":lambda:s(-1,k[-1]+ord(field[p[0]-1][p[1]])),"a":lambda:s(-1,k[-1]+ord(field[p[0]+1][p[1]])),"D":lambda:k.pop(),"d":lambda:k.append(k[-1]),"E":lambda:field[p[0]-1].__setitem__(p[1],chr(26)),"e":lambda:field[p[0]+1].__setitem__(p[1],chr(26)),"F":lambda:field[p[0]-1].__setitem__(p[1],chr(k.pop())),"f":lambda:field[p[0]+1].__setitem__(p[1],chr(k.pop())),"G":lambda:t(lambda: field[p[0]-1].__setitem__(p[1],input()[0]), lambda: field[p[0]-1].__setitem__(p[1],chr(26)), EOFError),"g":lambda:t(lambda: field[p[0]+1].__setitem__(p[1],input()[0]), lambda: field[p[0]+1].__setitem__(p[1],chr(26)), EOFError),"H":lambda:[p.__setitem__(1,p[1]-list(reversed(field[p[0]][0:p[1]])).index(chr(k[-1]))),r.__setitem__(0,2)],"h":lambda:r.__setitem__(0,2),"J":lambda:[y(p[0]+[l[0] for l in field[p[0]:]].index(chr(k[-1]))),r.__setitem__(0,1)],"j":lambda:r.__setitem__(0,1),"K":lambda:[y(p[0]-list(reversed([l[0] for l in field[0:p[0]]])).index(chr(k[-1]))),r.__setitem__(0,3)],"k":lambda:r.__setitem__(0,3),"L":lambda:[p.__setitem__(1,p[1]-field[p[0]][p[1]:].index(chr(k[-1]))),r.__setitem__(0,0)],"l":lambda:r.__setitem__(0,0),"P":lambda:print(end=field[p[0]-1][p[1]]),"p":lambda:print(end=field[p[0]+1][p[1]]),"q":lambda:exit(),"R":lambda:s(-1,k[-1]-ord(field[p[0]-1][p[1]])),"r":lambda:s(-1,k[-1]-ord(field[p[0]+1][p[1]])),"S":lambda:k.append(ord(field[p[0]-1][p[1]])),"s":lambda:k.append(ord(field[p[0]+1][p[1]])),"X":lambda:r.__setitem__(0,(r[0]+3)%4) if k[-1]<0 else None,"x":lambda:r.__setitem__(0,(r[0]+1)%4) if k[-1]<0 else None,"#":lambda:r.__setitem__(0,1) if p==[0,0] and field[0,1] == "!" else None}.get(field[p[0]][p[1]],lambda:[print("[ARGH!]"),exit()])(),[lambda:x(p[1]+1),lambda:y(p[0]+1),lambda:x(p[1]-1),lambda:y(p[0]-1)][r[0]]()], None))

argh('''j       world
lppppppPPPPPPsrfj
 hello,      *  j
              qPh''')