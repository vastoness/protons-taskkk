users = {}

def register_user(username):
    if username in users:
        print(f"Username '{username}' already exists. Please choose a different one.")
        return

    users[username] = {"username": username, "chat_history": []}
    print(f"Welcome, {username}! You are now registered.")

def send_message(sender, recipient, message):
    if recipient not in users:
        print(f"User '{recipient}' not found.")
        return

    users[sender]["chat_history"].append(f"Sent to {recipient}: {message}")
    users[recipient]["chat_history"].append(f"From {sender}: {message}")
    print(f"Message sent from {sender} to {recipient}.")

def view_messages(username):
    if not users[username]["chat_history"]:
        print(f"{username}, you have no messages in your history.")
        return

    print(f"Chat History for {username}:")
    for message in users[username]["chat_history"]:
        print(message)

while True:
    action = input("Enter action (register, send, view, quit): ")
    if action == "register":
        username = input("Enter username: ")
        register_user(username)
    elif action == "send":
        sender = input("Enter your username: ")
        if sender in users:
            recipient = input("Enter recipient username: ")
            message = input("Enter message: ")
            send_message(sender, recipient, message)
        else:
            print(f"Username '{sender}' not found. Please register first.")
    elif action == "view":
        username = input("Enter username to view history: ")
        if username in users:
            view_messages(username)
        else:
            print(f"Username '{username}' not found. Please register first.")
    elif action == "quit":
        print("Exiting chat system.")
        break
    else:
        print("Invalid action. Please try again.")