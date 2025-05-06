from flask import Flask, render_template

app = Flask(__name__)

# Данные о компаниях (можно заменить на запрос к БД)
companies = [
    {
        "name": "Sokolov",
        "description": "Один из крупнейших ювелирных брендов России, известный современными дизайнами.",
        "image": "Sokolov.webp"
    },
    {
        "name": "Adamas",
        "description": "Сеть ювелирных магазинов, предлагающая украшения из золота и драгоценных камней.",
        "image": "Adamas.png"
    },
    {
        "name": "585 Gold",
        "description": "Популярный бренд с широким ассортиментом украшений по доступным ценам.",
        "image": "585Gold.jpg"
    }
]

@app.route('/')
def home():
    return render_template('home.html', companies=companies)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
