import sys

s = set()
for _ in range(int(sys.stdin.readline())):
    name, t = sys.stdin.readline().split()
    if t == "enter":
        s.add(name)
    elif t == "leave":
        s.remove(name)
for a in sorted(s, reverse=True):
    print(a)