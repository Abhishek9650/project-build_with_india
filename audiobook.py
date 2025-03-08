import pyttsx3
import tkinter as tk
def main():
    # Open the text file containing the book
    from tkinter import filedialo
    root = tk.TK()
    root.withdraw() #hide main window
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
    else:
        print("No file selected.")
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Prompt the user to choose voice gender
    print("Choose voice gender:")
    print("1. Male")
    print("2. Female")
    voice_choice = int(input("Enter your choice (1 or 2): "))

    # Set voice gender based on user's choice
    if voice_choice == 1:
        voice_index = 0  # Male voice
    elif voice_choice == 2:
        voice_index = 1  # Female voice
    else:
        print("Invalid choice. Defaulting to female voice.")
        voice_index = 1  # Default to female voice

    # Prompt the user to choose speech rate
    while True:
        try:
            speech_rate = int(input("Enter speech rate (100 to 400, default is 150): "))
            if 100 <= speech_rate <= 400:
                break
            else:
                print("Speech rate must be between 100 and 400.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Set properties for voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', speech_rate)

    # Convert text to speech
    engine.say(book_text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
