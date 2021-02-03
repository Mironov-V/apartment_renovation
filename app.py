from datetime import timedelta
from app.controllers.bot import Chat
from flask import Flask
from flask import render_template
from app.shark.models.models import Makemigrations


app = Flask(__name__)

@app.route('/')
def index():
    return render_template(template_name_or_list="index.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)