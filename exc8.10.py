def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print(f"Sending: {message}")
        sent_messages.append(message)


messages = ["Halo!", "Apa kabar?", "Semangat!"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Original list:", messages)
print("Sent messages:", sent_messages)
