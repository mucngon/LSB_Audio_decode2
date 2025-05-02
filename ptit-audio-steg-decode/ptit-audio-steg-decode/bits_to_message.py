def bits_to_message(bits):
    bit_str = ''.join(map(str, bits))
    chars = []

    for i in range(0, len(bit_str), 8):
        byte = bit_str[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)

if __name__ == "__main__":
    from extract_lsb import extract_lsb_bits
    bits = extract_lsb_bits("output.wav")
    message = bits_to_message(bits)
    print(message[:100])
