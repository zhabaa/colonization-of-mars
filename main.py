from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1> Миссия Колонизация Марса </h1>"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    return "</br>".join(
        [
            "Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!",
        ]
    )


@app.route("/image_mars")
def image_page():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title> Привет, Марс! </title>
        <style>
            img {{
                width: 50%;
                height: 50%;
            }}
        </style>
    </head>
    <body>
        <h1> Жди нас, Марс! </h1>
        <img src="{url_for('static', filename='img/mars.png')}" alt="mars.png"> 
        <p> Вот она какая, красная планета </p>
    </body>
    </html>
    """

@app.route('/promotion_image')
def promotion_image():
    with open('static/promotion_page.html', 'r', encoding='utf-8') as html_file:
        html = html_file.read()

        html = html.replace('{{style.css}}', f'{url_for('static', filename='css/style.css')}')
        html = html.replace('{{mars_image}}', f'{url_for('static', filename='img/mars.png')}')

    return html


    

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1", debug=True)
