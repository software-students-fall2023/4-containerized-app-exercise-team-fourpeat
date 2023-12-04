""" Listens to audio from microphone for an animal and prints out the animal's sound in response"""
import sys
import speech_recognition as sr
import animal_db

recognizer = sr.Recognizer()


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
    animal_db.db["animal_sounds"].insert_one(data)


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
    elif "pig" in text.lower():
        save_to_database("pig", "oink")
    elif "goodbye" in text.lower():
        save_to_database("machine learning client", "Goodbye!")
        return True
    else:
        save_to_database("machine learning client", "I can't understand.")
    return False


def main(audio):
    """main script function"""
    # audio = sr.AudioFile(audio_file_path)
    # with audio as source:
    #    audio_data = recognizer.record(source)
    # text = convert_voice_to_text(audio_data)
    end_program = process_voice_command(audio)
    if end_program:
        print("done")


if __name__ == "__main__":
    main(sys.argv[1])
