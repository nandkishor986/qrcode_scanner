# Required Packages:- Pillow, qrcode. 

from flask import Flask, send_file
import qrcode
import qrcode.constants
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def generate_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data("https://up-in-clouds.web.app/")
    qr.make(fit=True)

    image = qr.make_image(fill_color="yellow", back_color="blue")
    
    # Save image to memory (not disk)
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Force download
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

if __name__ == '__main__':
    app.run()
