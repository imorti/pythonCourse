message = input(">")

# If user puts in 'Good morning :-)' we respond in kind
words = message.split(' ')
emojis = {
    ":)": "😁",
    ":(": "😢"
}
output = ""

for word in words:
    output += emojis.get(word, word) + " "

print(output)