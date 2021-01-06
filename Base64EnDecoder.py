#!/usr/bin/python

import sys
import base64

def error_handle():
    print '[+] use: $python Base64EnDecoder.py -e [file] -o [file]'
    print '[+] use: $python Base64EnDecoder.py -d [file] -o [file]'
    sys.exit(1)

if len(sys.argv) != 5:
    error_handle()

try:
    input = open(sys.argv[2], 'rb').read()
except:
    print '[*] error: file does NOT exist.'
    sys.exit(1)

try:
    if sys.argv[1] == '-e':
        data = base64.b64encode(input)
    elif sys.argv[1] == '-d':
        data = base64.b64decode(input)
    else:
        print '[*] error: input option is \'-e\' or \'-d\'.'
        error_handle()
except:
    print '[*] error: incorrect padding'
    sys.exit(1)

if sys.argv[3] == '-o':
    output = open(sys.argv[4], 'wb')
    output.write("{\"data\":\""+data+"\"}")
else:
    print '[*] error: output option is \'-o\'.'
    error_handle()
