# import required modules
import subprocess

# ffmpeg -i resources/Welcome.mp3  -ar 16000 -ac 1  result.wav

input_file = "Welcome.mp3"
output_file = "result.wav"

# convert mp3 to wav file
subprocess.call(['ffmpeg', '-i', 'Welcome.mp3',
                 '-ar', '16000',
                 '-ac', '1',
                 'result.wav'])
