def get_hidden_message(full_message):
    if "###" in full_message:
        return full_message.split("###")[0]
    return None

if __name__ == "__main__":
    from extract_lsb import extract_lsb_bits
    from bits_to_message import bits_to_message

    bits = extract_lsb_bits("output.wav")
    full_message = bits_to_message(bits)
    hidden = get_hidden_message(full_message)

    if hidden:
        print(f"Tìm thấy thông điệp: {hidden}")
    else:
        print("Không tìm thấy thông điệp.")