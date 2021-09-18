# vigenere-cipher-python
This small repo consists of python code for encoding and decoding a message according to the vigenere cipher decryption method.  
It was written in November 2020, when I was a beginner trying to learn Python 3.  
I wrote it without looking anything up, so the code is definitely not optimal, and has not been tested extensively whatsoever so it may contain bugs.  

If you want to learn more about the vigenere cipher I suggest reading the wikipedia page: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher  

The encode method takes in the message that you want to encode as the first parameter, and the key as the second parameter. It returns the encoded message. For example: encode("This is a secret message", "hiddenkey") will return "Toqv lw n ciaymw pifceel".  
We can save this encoded message in a variable like so: encoded_message = encode("This is a secret message", "hiddenkey")  
Now we can decode it with the decode method which takes in the message to be decoded as the first parameter, and the key as the second. To continue the example:  
print(decode(encoded_message, "hiddenkey")) will print "This is a secret message" to the terminal. 


