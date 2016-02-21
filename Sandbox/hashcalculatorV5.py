#Author: Ronan Dunphy
#Mobile Device Forensics - Lab 3
#Objective: To create a script to check the integrity of a string or file by computing the hash code for SHA-1, SHA-256, SHA-512, SHA-3(256) and SHA-3(512).
#Developed using Python version 2.7 on Windows 10
#Hashlib patched to support SHA-3 using the pysha3-0.3.win32-py2.7.exe installer located at https://pypi.python.org/pypi/pysha3/

#import sys, string and hashlib module used for SHA-1, SHA-256, SHA-512 and patched module for SHA-3(256) and SHA-3(512).
import sys
import hashlib
from sha3 import sha3_256, sha3_512
import string
import os.path

f = open('output.txt','w')
sys.stdout = f

#user defined file path requested and attached to "inputFile" variable. If the file is in the same folder as script the file name is sufficient, otherwise enter full path to file.
inputFile = "MDF-SF1.docx"

#blocksize set to limit size of large files
BLOCKSIZE = 65536

    #"hash_object1" variable contents hashed using the hashlib encryption type defined. "inputFile" variable opened in binary mode to allow non text files.
hash_object1 = hashlib.sha1()
with open(inputFile, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hash_object1.update(buf)
        buf = afile.read(BLOCKSIZE)       

#"hash_object2" variable contents hashed using the hashlib encryption type defined. "inputFile" variable opened in binary mode to allow non text files.
hash_object2 = hashlib.sha256()
with open(inputFile, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
         hash_object2.update(buf)
         buf = afile.read(BLOCKSIZE)		     

#"hash_object3" variable contents hashed using the hashlib encryption type defined. "inputFile" variable opened in binary mode to allow non text files.
hash_object3 = hashlib.sha512()
with open(inputFile, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
         hash_object3.update(buf)
         buf = afile.read(BLOCKSIZE)		      

#"hash_object4" variable contents hashed using the hashlib encryption type defined. "inputFile" variable opened in binary mode to allow non text files.
hash_object4 = hashlib.sha3_256()
with open(inputFile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
             hash_object4.update(buf)
             buf = afile.read(BLOCKSIZE)		        

#"hash_object5" variable contents hashed using the hashlib encryption type defined. "inputFile" variable opened in binary mode to allow non text files.
hash_object5 = hashlib.sha3_512()
with open(inputFile, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
             hash_object5.update(buf)
             buf = afile.read(BLOCKSIZE)
		
#variables defined in previous section are printed to the screen in hexidecimal format.	
print ("The filename is: %s" % inputFile)
print("SHA-1: " + hash_object1.hexdigest())
print("SHA-256: " + hash_object2.hexdigest())
print("SHA-512: " + hash_object3.hexdigest())
print("SHA-3(256): " + hash_object4.hexdigest())
print("SHA-3(512): " + hash_object5.hexdigest())


 
