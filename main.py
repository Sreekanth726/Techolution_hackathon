# working opencv2 to save the files in the folder

import cv2
import numpy as np
import pyaudio
import wave

# Define the codec and create a VideoWriter object to save the output video in MP4 format
output_video_path = 'D://techolution//video_to_audio//video_capture//output.mp4'  # Change this to your desired output location with .mp4 extension
fourcc = cv2.VideoWriter_fourcc(*'X264')  # Use 'X264' codec for MP4
out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (640, 480))  # Adjust frame size and frame rate as needed

# Create a video capture object for your camera
vid_capture = cv2.VideoCapture(0)  # 0 represents the default camera, change it if necessary

if not vid_capture.isOpened():
    print("Error opening the camera")

# Audio setup
audio_output_path = 'D://techolution//video_to_audio//video_capture//output_audio.wav'  # Change this to your desired audio output location
audio_format = pyaudio.paInt16
audio_channels = 1
audio_rate = 44100
audio_chunk = 1024

audio = pyaudio.PyAudio()
audio_stream = audio.open(format=audio_format, channels=audio_channels, rate=audio_rate, input=True, frames_per_buffer=audio_chunk)
audio_frames = []

while True:
    # Capture frame-by-frame
    ret, frame = vid_capture.read()
    if ret:
        cv2.imshow('Frame', frame)

        # Write the frame to the output video file
        out.write(frame)

        # Record audio
        audio_data = audio_stream.read(audio_chunk)
        audio_frames.append(audio_data)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break

# Release the video capture and writer objects
vid_capture.release()
out.release()
cv2.destroyAllWindows()

# Save the audio as a WAV file
audio_stream.stop_stream()
audio_stream.close()
audio.terminate()

with wave.open(audio_output_path, 'wb') as wf:
    wf.setnchannels(audio_channels)
    wf.setsampwidth(audio.get_sample_size(audio_format))
    wf.setframerate(audio_rate)
    wf.writeframes(b''.join(audio_frames))
