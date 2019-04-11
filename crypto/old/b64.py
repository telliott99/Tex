lc = 'abcdefghijklmnopqrstuvwxyz'
uc = lc.upper()
dg = '0123456789'
cL = uc + lc + dg + '+/'
D = dict(zip(range(len(cL)),cL))

def encode_tripstr_to_bin(s):
    L = list()
    for c in s:
        x = ord(c)
        b = bin(x)[2:].zfill(8)
        L.append(b)
    b = ''.join(L)
    return b
    
def convert_bin_to_b64(b):
    rL = list()
    while b:
        rL.append(b[:6])
        b = b[6:]
    rL = [int(c,2) for c in rL]
    rL = [D[i] for i in rL]
    return rL
    
def encode_triplet(s):
    b = encode_tripstr_to_bin(s)
    b64 = convert_bin_to_b64(b)
    print b64
    
encode_triplet('Man')