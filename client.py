import xmlrpc.client
from datetime import datetime
import sys

# Proxy is created to communicate with the server
proxy = xmlrpc.client.ServerProxy('http://localhost:3000/')

# Variables
user_topic = ""
user_text = ""
note_name = ""
user_choice = 999

print("Welcome to your personal Note App!\n")
while(True):

    # While loop is used for the UI, options are below
    print("1) Add Note")
    print("2) Show notes")
    print("0) Quit")
    user_choice = input("Choose option: ")

    # Quit option
    if(user_choice == "0"):
        print("\n*Exiting...*\n")
        sys.exit(0)

    # Add Note option
    elif(user_choice == "1"):
        user_topic = input("Note topic: ")
        note_name = input("Note name: ")
        user_text = input("Note text: ")
        time_temp = datetime.now()
        timestamp = time_temp.strftime("%d/%m/%Y - %H:%M:%S")
        result = proxy.add_note(user_topic, note_name, user_text, timestamp)
        print(f"\n*{result}*\n")

    # Show notes option
    elif(user_choice == "2"):
        user_topic = input("Give a topic you are looking for: ")
        results = proxy.read_xml(user_topic)
        if(results == "Not Found"):
            print("\n*No Topic Found*\n")
        else:
            print(f"\nThe following notes were found under topic {user_topic}:\n")
            for result in results:
                print(f"*\nNote name: {result[0]}\nNote text: {result[1]}\nTimestamp: {result[2]}\n*\n")

    # Default for unknown command
    else:
        print("\n*Unknown command*\n")

