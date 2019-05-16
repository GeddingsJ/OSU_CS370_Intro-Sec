import mmh3
import sys
import time
from bitarray import bitarray

#Jacob Geddings Assignment 1 - Bloom Filter using mmh3
#Class Bloom Filter
class BloomFilter:
	#Initalize class
	def __init__(self, size, hash_count):
		self.size = size
		self.hash_count = hash_count
		self.bit_array = bitarray(self.size) #Start bit array based on size
		self.bit_array.setall(False) #Set entire array to 0
	
	#Adding n to filter
	def add(self, string):
		#to simulate multiple hashes we'll seed differently for each call of mmh3
		for seed in range(self.hash_count):
			index = mmh3.hash(string, seed) % self.size
			self.bit_array[index] = True

	#Checking if a value is in filter
	def checker(self, string):
		for seed in range(self.hash_count):
			index = mmh3.hash(string, seed) % self.size
			if self.bit_array[index] == False: #If hash returns 0 then it's definitely not here
				return False
		return True #If it gets to this point it is possibly here

#Main
#size of dictionary is 623518 values
#size for p = .05 and n size of 623518 is 3887770
size_of = 4000000

#Command line arguments, dictionary is first parameter, sample input is second
dictionary_input = sys.argv[1]
sample_input = sys.argv[2]

bf3 = BloomFilter(size_of, 3)
bf5 = BloomFilter(size_of, 5)

files = open(dictionary_input, 'r')
dictionary = [x.strip() for x in files.readlines()]
files.close()

files = open(sample_input, 'r')
sample = [x.strip() for x in files.readlines()]
files.close

sample = sample[1:]

for i in dictionary:
	bf3.add(i)
	bf5.add(i)

files = open('output3.txt', 'w+')
for i in sample:
	start = datetime.time()
	if bf3.checker(i):
		files.write('maybe\n')
	else:
		files.write('no\n')
	end = datetime.time()
	#print('BF3 one password check: ', end - start)
files.close()

files = open('output5.txt', 'w+')
for i in sample:
	start = time.clock()
	if bf5.checker(i):
		files.write('maybe\n')
	else:
		files.write('no\n')
	end = time.clock()
	#print('BF5 one password check: ', end - start)
files.close()

