from OpenSSL import crypto
from hashlib import md5
import sys
import os
if len(sys.argv) < 2:
    print('Usage: python3 prepare-crt.py <ca.crt>')
    sys.exit(1)
certfile = sys.argv[1]
extension = os.path.splitext(certfile)[1]
ca_construct = '{}.0'
cert = open(certfile, 'rb')
if extension == '.pem':
    # PEM format - ZAP uses this
    ca_obj = crypto.load_certificate(crypto.FILETYPE_PEM, cert.read())
elif extension == '.der':
    # DER format - Burp uses this
    ca_obj = crypto.load_certificate(crypto.FILETYPE_ASN1, cert.read())
else:
    print('Unknown certificate format')
    sys.exit(1)
md = md5(ca_obj.get_subject().der()).digest()
ret = (md[0] | (md[1] << 8) | (md[2] << 16) | md[3] << 24)
ca_file_hash = hex(ret).lstrip('0x')
path_with_cert = '/system/etc/security/cacerts/'+ca_construct.format(ca_file_hash)
print('Upload '+certfile+' to '+path_with_cert)
print('Example command:')
print('adb push '+certfile+' '+path_with_cert)
