import pyshark

# Đường dẫn tới file .pcapng đã lưu
file_path = r'E:\mang_may_tinh\ktra\baikiemtra.pcapng'

cap = pyshark.FileCapture(file_path, use_json=True, keep_packets=False)

for i, pkt in enumerate(cap):
    try:
        print(f"\n==== GÓI #{i+1} ====")

        # Tầng 2: Data Link (Ethernet)
        if 'eth' in pkt:
            print("Tầng 2 - MAC nguồn:", pkt.eth.src)
            print("Tầng 2 - MAC đích :", pkt.eth.dst)

        # Tầng 3: Network (IP)
        if 'ip' in pkt:
            print("Tầng 3 - IP nguồn  :", pkt.ip.src)
            print("Tầng 3 - IP đích   :", pkt.ip.dst)
            print("Tầng 3 - Giao thức :", pkt.ip.proto)

    except Exception as e:
        print(f"Lỗi tại gói #{i+1}: {e}")
    
    # Giới hạn số gói để dễ xem (tuỳ chọn)
    if i >= 10:
        break