Exposure to using a bloom filter for weak password detection.

Assignment 1 was built on school flip servers with python.

running 'make' from makefile will install:
	mmh3 to user
	bitarray to user

TO RUN:
	python bloom_filter.py dictionary.txt sample_input.txt

WHERE:
	dictionary.txt is file of values to be added to filter
		NOTE: leading and trailing spaces and newlines are stripped.
	sample_input.txt is file of values to check if present in filter

OUTPUT:
	File will be made / overwrite for output3.txt and output5.txt

Resources:
	Murmurhash3:
		https://pypi.python.org/pypi/mmh3/2.5.1
	BitArray:
		https://pypi.python.org/pypi/bitarray
	
Assignment Questions:
	a. Chose to use Murmurhash3 as my function of choice and it
	uses non-cryptographic functions in an effort to increase
	speed at the expense of being less secure. It uses a 32bit default
	value. Size of 'm' was based off of:
	
		-(623518 ln 0.05) / (ln 2)^2

	Where the size of dictionary.txt is 623518 and p is 0.05. 
	This resulted in a rounded up total of 4 million for size m.

	b. On average the five hash takes 2 microseconds longer to complete.
	An example of this is the seventh value of the sample checks. This is due
	to the fact that if an item may be in the list it needs to check against
	two additional functions.

	c. For 3 hash: 5.211% chance of false positive, 0% false negative.
	   For 5 hash: 4.648% chance of false positive, 0% false negative.

	d. Increasing hash functions or increasing bit array size.