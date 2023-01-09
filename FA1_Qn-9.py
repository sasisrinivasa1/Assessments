def reverse(output):
    output = output[::-1]
    return output

# text = input("User Input :: ")
text = "abc123def"
output = text[0:3] + text[4:]
print(reverse(output))