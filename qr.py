import qrcode,time
#qr=qrcode.make("www.adityabakare.cf")
#qr.save('myQR.png')
qr=qrcode.QRCode(
    version=1,
    box_size=15,
    border=5

)
data=time.asctime( time.localtime(time.time()))
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black', back_color='white')
img.save('1234.jpg')

