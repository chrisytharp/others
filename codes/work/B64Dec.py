import base64

file = open("/Users/christophertharp/Downloads/Encodedflag.txt", "r")

encoded = file.read()

decoded = base64.decodedstring(encoded)

print(decoded)
