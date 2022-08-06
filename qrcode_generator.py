# basic code
"""
import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=RgY6IDcwaqM")
img.save("ayan.png")
"""
#advanced
import qrcode as qr
from PIL import Image
qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data('https://www.youtube.com/')
qr.make(fit=True)
qr_img = qr.make_image(fill_color="blue", back_color="black")
qr_img.save('color_qrcode.png')