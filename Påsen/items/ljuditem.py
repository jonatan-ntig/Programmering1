import numpy as np
import sounddevice as sd
from items.påsitem import Item

class LjudItem(Item):
    def __init__(self):
        duration = 5
        sample_rate = 44100
        print("Spelar in ljud...")
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        print("Inspelning klar.")
        super().__init__("ljud", recording)

    def __str__(self):
        sample_rate = 44100
        width = 60

        blocks = " ▂▃▄▅▆▇█"

        samples = np.asarray(self.innehåll).flatten()
        if len(samples) == 0:
            return "[Inget ljud]"

        chunks = np.array_split(np.abs(samples), width)
        peaks = [chunk.max() if len(chunk) > 0 else 0 for chunk in chunks]
        max_peak = max(peaks) or 1.0

        bars = "".join(blocks[int((p / max_peak) * (len(blocks) - 1))] for p in peaks)
        duration = len(samples) / sample_rate
        return f"ID: {self.id}, Typ: Ljud, Storlek: {duration:.1f}s\n{bars}"

    def open(self):
        print("Spelar upp ljud...")
        sd.play(self.innehåll, samplerate=44100)
        sd.wait()
