import base64, struct
import rsa
import modinv

e = 17
p = 151
q = 211
n = p*q  # 31861
phi = (p-1)*(q-1)  # 31500
d = modinv.modinv(e,phi)  # 1853
d*e % phi  # 1

def test():
    print e,p,q
    print n,phi
    print d, d*e % phi, phi%e

#test()

# http://stuvel.eu/files/python-rsa-doc
pk = rsa.PrivateKey(n,e,d,p,q)
pbk = rsa.PublicKey(n,e)
print pbk
pbdata = pbk.save_pkcs1(format='PEM')
print pbdata
# PKCS#1 RSAPublicKey* (PEM header: BEGIN RSA PUBLIC KEY)

def test2():
    b64 = pbdata.strip().split('\n')[1] # 'MAcCAnx1AgER'
    print b64

    for c in base64.b64decode(b64):
        h = struct.unpack('B',c)[0]
        print h,
    print
    
#test2()
# 48 7 2 2 124 117 2 1 17

# 2 124 117 means two bytes
# 124*256 + 117 = 31861 = n
# 1 17 means one byte with value 17, = e

# what are the other values?
# it's too complicated
# http://tools.ietf.org/html/rfc3447

pdata = pk.save_pkcs1(format='PEM')

def test3():
    print pdata
    b64 = pdata.strip().split('\n')[1]
    for c in base64.b64decode(b64):
        h = struct.unpack('B',c)[0]
        print h,
    print

test3()

# 48 32 2 1 0 2 2 124 117 2 1 17 2 2 7 61 
# 2 2 0 151 2 2 0 211 2 1 53 2 2 0 173 2 1 73

# 48 32
# 2 1 0 ??
# we see again 
# 2 2 124 117
# 124*256 + 117 = 31861 = n
# 2 1 17
# 17 = e
# 2 2 7 61
# 7*256 + 61 = 1853 = d
# 2 2 0 151
# 151 = p
# 2 2 0 211
# 211 = q
# 2 1 53 ??
# 2 2 0 173 ??
# 2 1 73 ??




