import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="data/recordings/patient.wav", duration=10):
    sample_rate = 44100
    print("Recording...")

    recording = sd.rec(int(duration * sample_rate),
                       samplerate=sample_rate,
                       channels=1)

    sd.wait()

    write(filename, sample_rate, recording)
    print("Recording saved:", filename)

    return filename