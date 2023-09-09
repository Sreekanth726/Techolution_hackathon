## audio to text is workdin, need to work on the accuracy

import os
import speech_recognition as sr

# Function to transcribe audio and save the transcription to a text file
def transcribe_audio(audio_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        # Load the audio file
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)

        # Attempt transcription using the Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data, show_all=True)
            if not text:
                # If Google API result is empty, try the Sphinx engine
                text = recognizer.recognize_sphinx(audio_data)

        except sr.UnknownValueError:
            # If both engines fail to recognize, print an error message
            print("Both recognition engines could not understand audio")
            return

        # Create a text file name by replacing the audio file extension with '.txt'
        text_file_name = os.path.splitext(os.path.basename(audio_file_path))[0] + '.txt'

        # Get the directory where the audio file is located
        output_folder = os.path.dirname(audio_file_path)

        # Create the full path for the text file
        text_file_path = os.path.join(output_folder, text_file_name)

        # Save the transcription to the text file
        with open(text_file_path, 'w') as text_file:
            text_file.write(text)

        print(f"Transcription saved to: {text_file_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    audio_file_path = "D://techolution//video_to_audio//video_capture//output_audio.wav"  # Replace with the path to your audio file
    transcribe_audio(audio_file_path)
