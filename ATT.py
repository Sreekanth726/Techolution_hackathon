
import moviepy.editor as mp
import speech_recognition as sr

# Load the video
video = mp.VideoFileClip("C://Users//srika//OneDrive//Desktop//Sree//Hello WD//Hackthon//test_audio.mp4")

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("wave.wav")

# Initialize recognizer
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile("wave.wav") as source:
	data = r.record(source)

# Convert speech to text
text = r.recognize_google(data)

# Print the text
print("\nThe resultant text from video is: \n")
print(text)
with open('readme.txt', 'a') as f:
        f.write(''.join(text))
