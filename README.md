## Transcribing longer audio clips

The Command and GUI tools perform transcription on long wav files.
They take in a wav file of any duration, use the WebRTC Voice Activity Detector (VAD)
to split it into smaller chunks and finally save a consolidated transcript.

#### 0.1 Download Deepspeech 
Either clone from git via git clone, or Download a version from the release page

For the next steps we assume you have extracted the files to `~/Deepspeech`

### 1. Command line tool

The command line tool processes a wav file of any duration and returns a trancript
which will the saved in the same directory as the input audio file.

The command line tool gives you control over the aggressiveness of the VAD.
Set the aggressiveness mode, to an integer between 0 and 3.
0 being the least aggressive about filtering out non-speech, 3 is the most aggressive.

```
(venv) ~/Deepspeech/examples/vad_transcriber
$ python3 audioTranscript_cmd.py --aggressive 1 --audio ./audio/guido-van-rossum.wav --model ./models/0.4.1/


Filename                       Duration(s)          Inference Time(s)    Model Load Time(s)   Scorer Load Time(s)
sample_rec.wav                 13.710               20.797               5.593                17.742

```

    ffmpeg -i file.mp3  -ar 16000 -ac 1  outfile.wav
