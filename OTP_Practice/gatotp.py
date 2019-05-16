import struct
import time
import base64
import hmac
import os
import hashlib

key = 'abcdabcdabcdabcd'

print "Key: ", key

#Returns time in seconds in floating point
timer = int(time.time() / 30) #30 second interval and truncated to integer form

#Model based on RFC 3548 - decode a base 32 encoded string
#Given the presence of lowercase letters, casefold was enabled.
#Produces a new string that is of equal length to our final key.
key_temp = base64.b32decode(key, casefold = True)

#Create a string formatted by the struct as such:
# '>' indicates big-endian form
# 'Q' indicates unsigned long long integer, size of 8
struct_temp = struct.pack(">Q", timer) #convert timer into its raw byte form

#HMAC hashing based on the previous 32 decode of the key and the reassortment of our timer
#Uses HMAC-SHA1 as indicated by last argument of hmac.new()
hmac_hash = hmac.new(key_temp, struct_temp, hashlib.sha1).digest() #generate hmac hash based on timestamp

#take 4 bytes from digest and converts to unicode, order based on least-significant-bit
# -1 value allows the string to wrap around to the last value of the string
# 15 allows us to take only the lower 4 bits of the last value
# 	Example when running: last value of 'X' converted into binary is 0111 1000, take last four of 1000 
#	which is numerical value of 8, set offset to equal the value 8
offset = ord(hmac_hash[-1]) & 15
trunc = hmac_hash[offset:offset+4] 

#extract code from the 4 bytes pulled
#convert for big-endian and unsigned long
response = struct.unpack(">L", trunc)[0]

#Ensure value is positive
abs(response)
#Mod operation
response %= 1000000;

#TOTP key
print response
