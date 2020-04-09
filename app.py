from flask import Flask, render_template, Response, url_for
from camera import VideoCamera
import datetime

app = Flask(__name__)

def gen(_camera, snap):
    while True:
        frame = _camera.get_frame(False)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    snap = False
    return Response(gen(VideoCamera(), snap),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def hello_world():
    print(datetime.date.today())
    mytime=datetime.date.today()
    return render_template('page1.html', test=mytime)


@app.route('/page')
def secondpage():
    return "page2"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
