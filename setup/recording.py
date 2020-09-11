import pyaudio
import time
import wave


def start_recording():
        chunk = 1024
        sample_format = pyaudio.paInt16
        channels = 2
        fs = 44100
        seconds = 3
        filename = "./require/roll_call.wav"
        
        p = pyaudio.PyAudio()
        
        print("Recoding : \n")
        input("Press ENTER to start 3 second recording\n\n(Please speak closely and loudly!!)\n")
        
        stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)
        
        frames = []

        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        
        p.terminate()
        
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        
