import time
import atexit
from flask import Flask,render_template
import qrcode
from apscheduler.schedulers.background import BackgroundScheduler
app=Flask(__name__)

@app.route('/')
def my_qr():
    qr=qrcode.QRCode(
    version=1,
    box_size=15,
    border=5

    )
    data=time.asctime(time.localtime(time.time()))
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill='black', back_color='white')
    img.save('static/xyz.jpg')
    result='xyz.jpg'
    return render_template('random.html',result=result)


   

scheduler = BackgroundScheduler()
scheduler.add_job(func=my_qr, trigger="interval", seconds=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
if __name__=="__main__":
    app.run()

