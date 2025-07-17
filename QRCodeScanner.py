# Required Packages:- Pillow, qrcode. 

import qrcode
from PIL import Image
import qrcode.constants 

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=4)

qr.add_data("https://up-in-clouds.web.app/")

qr.make(fit=True)

image= qr.make_image(fill_color="yellow", back_color="blue")

image.save("upinclouds.png")