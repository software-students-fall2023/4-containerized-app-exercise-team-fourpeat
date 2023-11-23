""" Listens to audio from microphone for an animal and prints out the animal's sound in response"""
import speech_recognition as sr

recognizer = sr.Recognizer()

"""Captures audio from microphone"""
def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

"""Converts audio to string"""
def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

"""Proccesses string to animal sound response"""
def process_voice_command(text):
    if "human" in text.lower():
        print("hi")
    elif "cat" in text.lower():
        print("meow")
    elif "dog" in text.lower():
        print("woof")
    elif "cow" in text.lower():
        print("moo")
    elif "bird" in text.lower():
        print("chirp")
    elif "frog" in text.lower():
        print("ribbit")
    elif "snake" in text.lower():
        print("hisss")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    else:
        print("I didn't understand that command. Please try again.")
    return False

"""main script function"""
def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()
