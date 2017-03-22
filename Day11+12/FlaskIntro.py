from flask import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for("foodblog"))

number_of_visiter = 0
girl_list = [
    {
        "src": "http://68.media.tumblr.com/c2b359d90b868247565a37b4f70ea2d9/tumblr_omu6agTv6b1qbd81ro1_1280.jpg",
        "title": "12343 by Đinh Văn Linh ♥",
        "tags": "#girl xinh#pretty girl#vietnam girl#beautiful girl photo#photography",
        "price": "135. 500 đ"
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

food_list = [
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "Bánh rán chanh vắt khổng lồ",
        "title": "Món bánh rán đậm chất vỉa hè Việt Nam được đưa vào chế biến cùng nguyên liệu tinh túy từ sữa dừa và hoa nhài, tạo nên sự khác biện giữa không gian và thời gian",
        "price": "135. 500 đ"
    },
    {
        "src": "http://lovelyindeed.com/wp-content/uploads/2016/10/pumpkin-donut-holes-1-450x675.jpg",
        "name_food": "aaa",
        "title": "bbb",
        "price": "135. 500 đ"
    },
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "aaa",
        "title": "bbb",
        "price": "135. 500 đ"
    },
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "aaa",
        "title": "bbb",
        "price": "135. 500 đ"
    },
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "aaa",
        "title": "bbb",
        "price": "135. 500 đ"
    },
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "aaa",
        "title": "bbb",
        "price": "135. 500 đ"
    },
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "aaa",
        "title": "bbb",
        "price": "135. 500 đ"
    },
    {
        "src": "http://liztraks.com/ltphotography/wp-content/uploads/2016/01/2-1-450x675.jpg",
        "name_food": "aaa",
        "title": "bbb",
        "price": "135. 500 đ"
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


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/css_demo')
def css_demo():
    return render_template("cssdemo.html")


@app.route('/w3cssdemo')
def w3css_demo():
    return render_template("w3cssdemo.html")


@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html", food_list=food_list)


if __name__ == '__main__':
    app.run()
