#!/usr/bin/python3 
from Crypto.Cipher import AES
from ctypes import CDLL
import datetime 
import base64 

a = base64.b64decode('qQwrmkzuhJv6fzCF2XsxuaB+ZBtMEH+Cd3fpTgJpEM8=')
b = base64.b64decode('FjmNRmlNzMZYK8TbIItuVA==')
c = base64.b64decode('8XvXFKhm8YFfQShtVXcNZh5F8q0zBJMTnfBSh33SEr8r4hMWb/E2VJq20QO2Byef')
cipher = AES.new(a, AES.MODE_CBC, b)
print(cipher.decrypt(c))
