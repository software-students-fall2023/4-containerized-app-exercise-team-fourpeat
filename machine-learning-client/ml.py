""" Listens to audio from microphone for an animal and prints out the animal's sound in response"""
import sys

sys.path.append("../")
import db
import speech_recognition as sr


recognizer = sr.Recognizer()


def capture_voice_input(timeout=5):
    """Captures audio from microphone with a specified timeout"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            if not audio:
                print("No audio detected. Please speak louder or try again.")
        except sr.WaitTimeoutError:
            print("Timeout occurred. No audio input received.")
            audio = None
    return audio


def convert_voice_to_text(audio):
    """Converts audio to string"""
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print(f"Error: {e}")
    return text


def save_to_database(animal, sound):
    """Saves animal sound into the MongoDB database"""
    data = {"animal": animal, "sound": sound}
    db.db.collection.insert_one(data)
    print(f"Saved sound '{sound}' for {animal} in the database.")


def process_voice_command(text):
    """Proccesses string to animal sound response"""
    if "human" in text.lower():
        save_to_database("human", "hi")
    elif "cat" in text.lower():
        save_to_database("cat", "meow")
    elif "dog" in text.lower():
        save_to_database("dog", "woof")
    elif "cow" in text.lower():
        save_to_database("cow", "moo")
    elif "bird" in text.lower():
        save_to_database("bird", "chirp")
    elif "frog" in text.lower():
        save_to_database("frog", "rabbit")
    elif "snake" in text.lower():
        save_to_database("snake", "hisss")
    elif "goodbye" in text.lower():
        save_to_database("machine learning client", "Goodbye!")
        return True
    else:
        save_to_database("machine learning client", "I can't understand.")
    return False


def main():
    """main script function"""
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)


if __name__ == "__main__":
    main()
