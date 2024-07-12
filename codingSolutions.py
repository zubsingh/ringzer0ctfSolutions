# Hash Me Solution
import requests
import hashlib

x = requests.get('http://challenges.ringzer0ctf.com:10013/')
if '----- BEGIN MESSAGE -----' in x.text:
    start = x.text.index('----- BEGIN MESSAGE -----') + len('----- BEGIN MESSAGE -----') + 15 #15 is required to exclude the br html tag and some newlines, the same goes for the other 15 on the next line
    stop = x.text.index('----- END MESSAGE -----') - 15
    message = x.text[start:stop]
    result = hashlib.sha512(message.encode('utf-8')).hexdigest()
    url = 'http://challenges.ringzer0team.com:10013/?r=' + result
    y = requests.get(url)
    print(y.text)

# Hash me again Solution

# Make a GET request to the challenge URL
response = requests.get('http://challenges.ringzer0team.com:10014/')

# Check if the response contains the specific message markers
if '----- BEGIN MESSAGE -----' in response.text:
    # Find the start index of the binary message
    start_index = response.text.index('----- BEGIN MESSAGE -----') + len('----- BEGIN MESSAGE -----') + 15
    # Find the stop index of the binary message
    stop_index = response.text.index('----- END MESSAGE -----') - 15
    # Extract the binary message from the response text
    binary_message = response.text[start_index:stop_index]

    # Initialize an empty string to store the characters
    char_message = ''
    
    # Iterate over the binary message in steps of 8 to convert each byte
    for i in range(0, len(binary_message), 8):
        # Convert each 8-bit substring to an integer
        byte = int(binary_message[i:i+8], 2)
        # Convert the integer to a character and append to char_message
        char_message += chr(byte)
    
    # Hash the character message using SHA-512
    hashed_message = hashlib.sha512(char_message.encode('utf-8')).hexdigest()

    # Construct the URL with the hashed result as a query parameter
    url = 'http://challenges.ringzer0team.com:10014/?r=' + hashed_message
    
    # Make a GET request to the constructed URL
    response = requests.get(url)
    
    # Print the response text from the second request
    print(response.text)
