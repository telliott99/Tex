import binascii
import rsa
import utils

data = utils.load_data('kf')
priv_key = rsa.PrivateKey.load_pkcs1(data)

# having trouble with formats
# pubdata = utils.load_data('kf.pub.pem')
# pubkey = rsa.PublicKey.load_pkcs1(pubdata)

# but this works
k = priv_key
pub_key = rsa.PublicKey(k.n,k.e)

def test():
    print 'e', k.e
    print 'p', k.p
    print 'q', k.q
    print 'n', k.n
    print 'd', k.d

# test()

m = 'hello world'
c = rsa.encrypt(m,pub_key)
p = rsa.decrypt(c,priv_key)
print p

crypto = rsa.encrypt('\x00\x00\x00\x00\x01', pub_key)
print binascii.hexlify(crypto)
p = rsa.decrypt(crypto, priv_key)
print binascii.hexlify(p)
