def emoji_converter(message_for_emoji):
    words = message.split()
    emojis = {
        "(:": "🥰",
        "):": "😥",
        "enjoy": "😍"
    }
    output = ""
    for item in words:
        output += emojis.get(item, item) + " "
    return output


message = input("> ")
result = emoji_converter(message)
print(result)
