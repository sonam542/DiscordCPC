import random
def handle_response(message):
    themessage = message.lower()

    if themessage == "hello":
        return "yo what's up"
    
    if themessage == "roll":
        return str(random.randint(1,6))
    
    