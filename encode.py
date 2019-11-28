from qrtools import QR
my_qr=QR(filename='/home/first-flask-app/x1.jpg')
my_qr.decode()
print(my_qr.data)