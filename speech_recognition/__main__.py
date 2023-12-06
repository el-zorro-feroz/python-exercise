import speech_recognition as sr


if __name__ == "__main__":
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        data = r.recognize_sphinx(audio)
        print(f"You said: {data}")
    except sr.UnknownValueError:
        print("Could not understand what you say")
    except sr.RequestError as e:
        print(f"Internal error: {e}")

