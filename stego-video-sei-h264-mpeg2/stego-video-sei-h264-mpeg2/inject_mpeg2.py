def inject_user_data(input_path, output_path, message):
    start_code = b'\x00\x00\x01\xb2'  # MPEG-2 user_data_start_code
    payload = message.encode('utf-8') + b'\x00'  # null-terminated string
    user_data_packet = start_code + payload

    with open(input_path, 'rb') as f:
        video_data = f.read()

    # Tìm sequence header (0x000001B3) để chèn user_data vào sau đó
    insert_pos = video_data.find(b'\x00\x00\x01\xb3')
    if insert_pos == -1:
        raise Exception("Không tìm thấy sequence_header!")

    # Chèn user_data ngay sau sequence_header
    new_video_data = (
        video_data[:insert_pos + 4] +
        user_data_packet +
        video_data[insert_pos + 4:]
    )

    with open(output_path, 'wb') as f:
        f.write(new_video_data)

    print(f"[+] Đã chèn thông điệp '{message}' vào '{output_path}'")


if __name__ == "__main__":
    inject_user_data("kitten_mpeg2.mpg", "stego_kitten_mpeg2.mpg", "Kin Cha Na Sa rang he")
