Programming Assignment 3 - TOTP Implementation
	Student: 	Jacob Geddings
	Language: 	Python
	GA App: 	Only have access to iOS variant

TO RUN:
	INPUT:
		python gatotp.py

RESULT:
	First line will be the 'secret' key that the TOTP uses
	Second line will be the 'code' that will match the GA app

Python Writeup:
	Due to using Python the programming assignment requirements also include a writeup detailing 
	how TOTP operates.

	To begin, I'll discuss the function that TOTP is an expansion of, HOTP. The HOTP algorithm 
	is based on the usage of HMAC-SHA-1 hashing that is then truncated to have a value 
	extracted that will then be the 'code' that is needed. For this to work a secret key and 
	counter must be defined and shared between both parties. With these two values the
	hash function will then generate a 20-byte string that is then truncated down to 4 bytes.
	With this truncated value we can now compute a code by perfoming a mod operation on it [1].
	
	It should be noted that my GA app was very specific in the key requirements, only accepting
	after I tried implementing a key of four sets of four alphabet characters. In addition when
	searching for how Python handles TOTP the mod operation was consistently used against the
	value of '1000000'. I did not exhaustively search for what form of keys work however, after
	getting one to be accepted I moved forward with the coding aspect of the assignment.

	Now TOTP relates to HOTP in every manner except the change of one variable, the counter. 
	Where HOTP needed an incrementer to only ensure that both client/server are on the same
	stage the TOTP method will instead replace that with a timer. This timer will be based
	on UNIX time of the day in seconds and function in the default 30-second interval. This 
	creates a scenario in which client/server will, for 30 second periods, continue to produce 
	the exact same access code. After this period has passed, the code is changed since the 
	timer has moved forward [2]. 

	TOTP carries an addition concern about network delay between both parties. If the code
	is sent with one second remaining before a new code is required there is a risk that
	the network delay will be greater than a second and invalidate the code. As such, 
	it is common practice to allow a brief grace period in sending codes such that a client
	can send with only a moment to spare. This grace period does need to be strict though, 
	too great of a window will result in more time for a brute force attack to get the code
	correct [2].

	Lastly, I will discuss the implementation of TOTP in this programming assignment. Within
	the code itself is several comment blocks that describe what the program is doing but I'll
	repeat it here. The program has a hard coded key that is assigned at the start of the 
	program and is printed out. Next up is the timer, using an import call we can construct 
	a time window with each run of the program that aligns with UNIX time in seconds. From here
	a common method I've observed online is to use the base64 import to construct a new string
	based on our intial key [3]. Problems ensued with padding errors as a result of using 
	alphabet characters, the added argument of casefold is included to remedy that [4].

	Next up is converting the timer through the calling of struct.pack() which converts the time
	into a string based on the modifiers '>' and 'Q' which signify big-endian and unsigned long 
	long integer respectively [5]. With these two strings constructed the HMAC function is called 
	and digests the input with SHA-1. The last 4 bytes of this returned value is then taken
	to be used as an offset for pulling a truncation of the hash string out [6]. This truncated value
	is then converted for big-endian and unsigned long, made absolute, and mod'ed by 1000000 [7].

	The final value from this process results in our code that is valid for approximately 30 seconds
	before the timer moves over and an entirely new code is generated through this process.

References:
	[1] RFC 4226 HOTP
		https://tools.ietf.org/html/rfc4226
	[2] RFC 6238 TOTP
		https://tools.ietf.org/html/rfc6238
	[3] Google Authenticator Implementation in Python
		https://stackoverflow.com/questions/8529265/google-authenticator-implementation-in-python
	[4] Base 64 - RFC 3548
		https://docs.python.org/2/library/base64.html
	[5] Struct
		https://docs.python.org/2/library/struct.html
	[6] Understanding Two-Step
		http://sahandsaba.com/two-step-verification-using-python-pyotp-qrcode-flask-and-heroku.html
	[7] Implementing Two-Factor
		https://patrickmn.com/security/you-can-be-a-twofactor-hero/