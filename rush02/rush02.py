import sys
def get_pair(line):
    key, sep, value = line.strip().partition(": ")
    return int(key), value

def make_dict():

    with open("dict.txt") as fd:
        d = dict(get_pair(line) for line in fd)
    return d

def get_c(cen, diz, u, d):
    if (cen == 0):
        return get_d(diz, u, d)
    else:
        return d[cen] + ' ' + d[100] + ' ' + get_d(diz, u, d) 
    
def get_d(diz, u, d):
    if (int(str(diz) + str(u))) in d and int(str(diz) + str(u)) != 0:
        return d[int(str(diz) + str(u))] + ' '
    elif (diz == 0):
        return (get_u(u, d))
    else:
        return d[diz * 10] + ' ' + get_u(u, d)
def get_u(u, d):
    if (u == 0):
        return '' 
    else:
        return d[u] + ' '


l = len(sys.argv[1])
n = sys.argv[1]
d = make_dict()
i = 0
c = 10**(l-(l%3)) if l % 3 else 10**(l-3)
s = ""
r = ""

for num in n:
    if num < '0' or num > '9':
        print("Entrez seulement des chiffres")
        exit()
if l > 12:
    print("Entrez un chiffre moindre que 999 999 999 999")
    exit()
while i < len(sys.argv[1]):
    if (l % 3 == 0):       
        r = get_c(int(n[i]), int(n[i + 1]), int(n[i + 2]), d)
        i += 3
    elif (l % 3 == 2):
        r += get_d(int(n[i]), int(n[i + 1]), d)
        i += 2
    else:
        r += get_u(int(n[i]), d)
        i += 1
    l -= l % 3
    s += r
    if (c >= 1000) and r != "":
        s += d[c] + ' '
    c /= 1000
print(s)
