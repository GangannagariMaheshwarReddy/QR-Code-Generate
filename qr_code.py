import qrcode

url = input("Enter the URL: ").strip()

file_path = r"C:\Users\Lenovo\Desktop\qrcode.png"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print("QR code is successfully generated")
