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


#Can you help me find the answer to this equation

# Define the URL to get the challenge message
url = 'http://challenges.ringzer0team.com:10032/'

# Make a GET request to the challenge URL
response = requests.get(url)

# Extract the message part between the markers
start_marker = '----- BEGIN MESSAGE -----'
end_marker = '----- END MESSAGE -----'
start_index = response.text.index(start_marker) + len(start_marker)
end_index = response.text.index(end_marker)
message = response.text[start_index:end_index].strip()

# Remove any HTML tags from the extracted message
import re
message = re.sub(r'<[^>]+>', '', message)

# Print the cleaned message
print('Cleaned message:', message)

# Parse the arithmetic expression
parts = message.split()
num1 = int(parts[0])  # First number
num2 = int(parts[2], 16)  # Hexadecimal number
num3 = int(parts[4], 2)  # Binary number

# Perform the arithmetic operations
result = num1 + num2 - num3

# Print the result
print('Result:', result)

# Construct the URL with the result
answer_url = f'http://challenges.ringzer0team.com:10032/?r={result}'

# Make a GET request to the answer URL
response = requests.get(answer_url)

# Print the response text
print(response.text)
