import sys
def get_pair(line):
    key, sep, value = line.strip().partition(": ")
    return int(key), value

def make_dict():

    with open("dict.txt") as fd:
        d = dict(get_pair(line) for line in fd)
    return d

def get_c(c, diz, u, d):
    return d[c] + ' ' + d[100] + ' ' + get_d(diz, u, d) 
    
def get_d(diz, u, d):
    if (int(str(diz) + str(u))) in d:
        return d[int(str(diz) + str(u))] + ' '
    else:
        return d[diz * 10] + ' ' + get_u(u, d)
def get_u(u, d):
    return d[u] + ' '


l = len(sys.argv[1])
n = sys.argv[1]
d = make_dict()
c = (10**(l-(l%3)))
i = 0
s = ""
while i < len(sys.argv[1]):
    if (l % 3 == 0):
        s += get_c(int(n[i]), int(n[i + 1]), int(n[i + 2]), d)
        i += 3
    elif(l % 3 == 2):
        s += get_d(int(n[i]), int(n[i + 1]), d)
        i += 2
    else:
        s += get_u(int(n[i]), d)
        i += 1
    if (c > 1):
        s += d[c] + ' '
    c /= 1000
    l -= l % 3
print(s)
