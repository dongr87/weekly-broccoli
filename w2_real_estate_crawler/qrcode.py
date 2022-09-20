import pyqrcode
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.google.com/search?q=qrcode&rlz=1C5CHFA_enUS951US951&oq=qrcode&aqs=chrome.0.0i131i433i512l2j0i10i131i433i512j0i512l4j0i10i131i433i512j0i512j0i131i433i512.8365j0j4&sourceid=chrome&ie=UTF-8"
  
# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png"
url.svg("qrcode.svg", scale = 8)