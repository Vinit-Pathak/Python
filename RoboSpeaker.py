import win32com.client as wincom
if __name__ == '__main__':
    print("Hello I'm a RoboSpeaker...")
    x = input("Enter what do you want me to speak...")
    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        if x == 'q':
            text = "bye bye friends"
            speak.Speak(text)
            break
        command = f"{x}"
        speak.Speak(command)