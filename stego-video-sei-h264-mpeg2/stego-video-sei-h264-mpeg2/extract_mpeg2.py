# extract_mpeg2_user_data.py

def extract_user_data(path):
    with open(path, 'rb') as f:
        data = f.read()

    pos = data.find(b'\x00\x00\x01\xb2')
    if pos == -1:
        print("[-] Không tìm thấy user_data_start_code")
        return

    end = data.find(b'\x00', pos + 4)  # tìm null byte kết thúc
    if end == -1:
        print("[-] Không tìm thấy kết thúc thông điệp")
        return

    msg = data[pos + 4:end].decode(errors='ignore')
    print(f"[+] Thông điệp được giấu: {msg}")


if __name__ == "__main__":
   extract_user_data("stego_kitten_mpeg2.mpg")

