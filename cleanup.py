import string

def easyreader(message):
    message_content = str(message.content)
    message_lower = message_content.lower()
    cleanup = message_lower.translate(str.maketrans('', '', string.punctuation))
    list_message = cleanup.split()
    return list_message