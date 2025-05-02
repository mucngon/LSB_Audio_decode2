import wave

def extract_lsb_bits(wav_path):
    with wave.open(wav_path, mode='rb') as song:
        frame_bytes = bytearray(song.readframes(song.getnframes()))
        return [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

if __name__ == "__main__":
    bits = extract_lsb_bits("output.wav")
    print("".join(map(str, bits[:100])))
