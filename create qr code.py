import qrcode
website_link='https://www.youtube.com/watch?v=YQ-qToZUybM&pp=ygULZGllIGZvciB5b3XSBwkJTgsBhyohjO8%3D'
qr=qrcode.QRCode(version=1, box_size=7,border=6)
qr.add_data(website_link)
qr.make()
img=qr.make_image(fill_color="black", back_color="white")
img.save('yt_qr.png')