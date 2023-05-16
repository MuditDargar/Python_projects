import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 2.0 created by mudit")
    while True:
      x = input("Enter what you want to speak: ")
      if x=="q":
        pyttsx3.speak("bye bye friend")
        break 
      command=f'"{x}"'
      pyttsx3.speak(command)

    # Initialize the pyttsx3 engine
    # engine = pyttsx3.init()
    # engine.say(x)
    # engine.runAndWait()
