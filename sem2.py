from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Card</title>
    <style>
        @import url('https://fonts.googleapis.com/css?family=Indie+Flower');
        @import url('https://fonts.googleapis.com/css?family=Amatic+SC');
        
        body {
            font-family: 'Indie Flower', cursive !important;
            background: rgb(92, 196, 157);
            margin: 0px;
            padding: 0px;
        }
        
        ::selection {
            background: transparent;
        }
        
        h4 {
            font-size: 26px;
            line-height: 1px;
            font-family: 'Amatic SC', cursive !important;
        }
        
        .color1 {color: rgb(255, 255, 255)}
        .card {
            color: rgb(1, 51, 67);
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 400px;
            background: rgb(250, 225, 76);
            transform-style: preserve-3d;
            transform: translate(-50%,-50%) perspective(2000px);
            box-shadow: inset 300px 0 50px rgba(0,0,0,.5), 20px 0 60px rgba(0,0,0,.5);
            transition: 1s;
        }
        
        .card:hover {
            transform: translate(-50%,-50%) perspective(2000px) rotate(15deg) scale(1.2);
            box-shadow: inset 20px 0 50px rgb(0,0,0), 0 10px 100px rgb(0,0,0);
        }
        
        .card:before {
            content:'';
            position: absolute;
            top: -5px;
            left: 0;
            width: 100%;
            height: 5px;
            background: rgb(255, 255, 255);
            transform-origin: bottom;
            transform: skewX(-45deg);
        }
        
        .card:after {
            content: '';
            position: absolute;
            top: 0;
            right: -5px;
            width: 5px;
            height: 100%;
            background: rgb(146, 162, 156);
            transform-origin: left;
            transform: skewY(-45deg);
        }
        
        .card .imgBox {
            width: 100%;
            height: 100%;
            position: relative;
            transform-origin: left;
            transition: .7s;
        }
        
        .card .bark {
            position: absolute;
            background: rgb(224, 225, 220);
            width: 100%;
            height: 100%;
            opacity: 0;
            transition: .7s;
        }
        
        .card .imgBox img {
            min-width: 300px;
            max-height: 400px;
        }
        
        .card:hover .imgBox {
            transform: rotateY(-135deg);
        }
        
        .card:hover .bark {
            opacity: 1;
            transition: .6s;
            box-shadow: 300px 200px 100px rgba(30, 40, 50) inset;
        }
        
        .card .details {
            position: absolute;
            top: 0;
            left: 0;
            box-sizing: border-box;
            padding: 0 0 0 10px;
            z-index: -1;
            margin-top: 70px;
        }
        
        .card .details p {
            font-size: 15px;
            line-height: 5px;
            transform: rotate(-10deg);
            padding: 0 0 0 20px;
        }
        
        .card .details h4 {
            text-align: center;
        }
        
        .text-right {
            text-align: right;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="imgBox">
            <div class="bark"></div>
            <img src="https://cdn1.cardly.net/card/1/5252c9b4-7bd3-e12c-fb32-9920d3584ec3/page1-r2-i9233-fcde9c73aaa66e3c1d0f606121111fbb.webp/vp/detail-card/1200">
        </div>
        <div class="details">
            <h4 class="color1">Dear Professor!</h4>
            <br>
            <p>Wishing you a speedy recovery and  </p>
            <p>brighter days ahead.! </p>
            <p>You're in our thoughts and prayers..! </p>
            <br>
            <p>With heartfelt wishes for your wellness</p>
            <br>
            <p class="text-right">ALBIN</p>
        </div>
    </div>
</body>
</html>
"""
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
