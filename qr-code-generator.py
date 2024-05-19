import qrcode
qr=qrcode.make(input("enter your information: "))
qr.save("qr-code-image.jpg")