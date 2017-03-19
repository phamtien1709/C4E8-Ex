from flask import *
from datetime import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for("oingonqua"))

number_of_visiter = 0
girl_list = [
    {
        "src": "http://68.media.tumblr.com/c2b359d90b868247565a37b4f70ea2d9/tumblr_omu6agTv6b1qbd81ro1_1280.jpg",
        "title": "12343 by Đinh Văn Linh ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "src": "http://68.media.tumblr.com/fdce8d90185f8f38a5f36a69b198a271/tumblr_ojqkfv1h7c1qbd81ro1_1280.jpg",
        "title": "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "src": "http://68.media.tumblr.com/333c275f13f585bb49a55f9e7b8fa9c8/tumblr_of8kztZ3QA1qbd81ro1_1280.jpg",
        "title": "DSC_2180 by mrSun_vn ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    },
    {
        "src": "http://68.media.tumblr.com/6707567f4007a0ebb6e342f37692da0b/tumblr_of8kzf8gMp1qbd81ro1_1280.jpg",
        "title": "IMG_7340 by Hải Nguyễn | Tell 0902990341 ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography"
    }
]


@app.route('/login')
def login():
    global number_of_visiter
    number_of_visiter += 1
    return render_template("login.html", girl_list=girl_list, number_visiter=number_of_visiter)


@app.route('/oingonqua')
def oingonqua():
    return render_template("oingonqua.html", girl_list=girl_list)


if __name__ == '__main__':
    app.run()
