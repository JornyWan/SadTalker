from pydub import AudioSegment


# Load your MP3 file
for i in range(6):
    mp3_audio = AudioSegment.from_file("{}.mp3".format(i), format="mp3")

    # Convert to WAV
    mp3_audio.export("{}.wav".format(i), format="wav")