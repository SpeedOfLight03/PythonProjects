import pyqrcode

# String which represent the QR code 
s = "https://www.youtube.com/channel/UCeO9hPCfRzqb2yTuAn713Mg"

# Generate QR code 
qr = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
qr.svg('myqr.svg', scale=8)