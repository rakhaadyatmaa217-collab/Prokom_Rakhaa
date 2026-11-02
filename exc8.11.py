def send_messages(messages, sent_messages):
    while messages:
        sent_messages.append(messages.pop(0))


messages = ["Halo!", "Apa kabar?", "Semangat!"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Messages:", messages)
print("Sent:", sent_messages)
