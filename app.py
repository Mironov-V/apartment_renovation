from os import mkdir
from PIL import Image
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from json import load
from termcolor import colored
from lib.mail import LibMail
from shark.orm import Shark
from shark.models.models import Makemigrations


app = Flask(__name__)
path = "/home/cosmobot/Freelance/apartment_renovation/"
Makemigrations().migrate()


@app.route("/admin", methods=["GET", "POST"])
def is_admin():
    # Create folders
    
    try:
        mkdir(f"{path}static/access/img/portfolio/")
    except FileExistsError:
        pass

    try:
        mkdir(f"{path}static/access/img/works/")
    except FileExistsError:
        pass

    try:
        mkdir(f"{path}static/access/img/comments/")
    except FileExistsError:
        pass

    # Connect is DataBase
    conn = Shark().connect()

    def add(conn=conn):
        if request.form.get('title_add') and request.files["file_add"]:
            # Finds is form
            title_add=request.form.get('title_add')
            file_add=request.files["file_add"].filename
            data=request.files["file_add"].read()
            # Upload file's
            with open(file=f"{path}static/access/img/portfolio/{file_add}", mode="wb+") as f_obj:
                f_obj.write(data)
                f_obj.close()
            # Save data
            Shark().insert(connect=conn['connect'], cursor=conn['cursor'], table='portfolio', 
                                            title=title_add, photo=f"{path}static/access/img/portfolio/{file_add}")

        if request.form.get('title_work_price_add') and request.form.get('work_price_add') and request.form.get('desk_work_price_add') and request.files["file_work_price_add"]:
            # Finds is form
            title_work_price_add=request.form.get('title_work_price_add')
            work_price_add=request.form.get('work_price_add')
            desk_work_price_add=request.form.get('desk_work_price_add')
            file_work_price_add=request.files["file_work_price_add"].filename
            data=request.files["file_work_price_add"].read()
            # Upload file's
            with open(file=f"{path}static/access/img/works/{file_work_price_add}", mode="wb+") as f_obj:
                f_obj.write(data)
                f_obj.close()
            # Save data
            Shark().insert(connect=conn['connect'], cursor=conn['cursor'], table='works', 
                        title=title_work_price_add, prices=work_price_add,
                        desk=desk_work_price_add, photo=f"{path}static/access/img/works/{file_work_price_add}")

        
        if  request.form.get("f_obj") and request.files["comment_add"]:
            # Finds is form
            comment_add=request.files["comment_add"].filename
            data=request.files["comment_add"].read()
            # Upload file's
            with open(file=f"{path}static/access/img/comments/{comment_add}", mode="wb+") as f_obj:
                f_obj.write(data)
                f_obj.close()
            # Save data
            Shark().insert(connect=conn['connect'], cursor=conn['cursor'], table='comments', photo=f"{path}static/access/img/comments/{comment_add}")
        

        if  request.form.get("question_add") and request.form.get("response_add"):
            # Finds is form
            question_add = request.form.get("question_add")
            response_add = request.form.get("response_add")
            # Save data
            Shark().insert(connect=conn['connect'], cursor=conn['cursor'], table='questions', 
                                                        title=question_add, desk=response_add)
    

    def update(conn=conn):
        pass

    
    def delete(conn=conn):
        if request.form.get('delete_portfolio'):
            # Finds is form
            delete_portfolio=request.form.get('delete_portfolio')
            # Save data
            Shark().delete(connect=conn['connect'], cursor=conn['cursor'], table='portfolio', 
                                                        value_key="id", value=delete_portfolio)

        if request.form.get('delete_works'):
            # Finds is form
            delete_works=request.form.get('delete_works')
            # Save data
            Shark().delete(connect=conn['connect'], cursor=conn['cursor'], table='works', 
                                                        value_key="id", value=delete_works)
        
        if request.form.get('delete_comments'):
            # Finds is form
            delete_comments=request.form.get('delete_comments')
            # Save data
            Shark().delete(connect=conn['connect'], cursor=conn['cursor'], table='comments', 
                                                        value_key="id", value=delete_comments)
        
        if request.form.get('delete_questions'):
            # Finds is form
            delete_questions=request.form.get('delete_questions')
            # Save data
            Shark().delete(connect=conn['connect'], cursor=conn['cursor'], table='questions', 
                                                        value_key="id", value=delete_questions)


    add()
    update()
    delete()

    portfolio = Shark().select_all(cursor=conn["cursor"], table="portfolio", param_search="*")
    works = Shark().select_all(cursor=conn["cursor"], table="works", param_search="*")
    comments = Shark().select_all(cursor=conn["cursor"], table="comments", param_search="*")
    questions = Shark().select_all(cursor=conn["cursor"], table="questions", param_search="*")

    return render_template(template_name_or_list="admin.html", portfolio=portfolio, 
                                works=works, comments=comments, questions=questions)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        send_to = load(open(f"{path}data.json", mode="r", encoding="UTF-8"))['send_to']
        if request.form.get('call-order'):
            title="Запрос звонка"

            msg=f"""
                <html>
                    <body>
                        <p>
                            Вам поступила заявка, клиент запрашивает звонок на номер:<br><a href="tel:{request.form.get('call-order')}">{request.form.get('call-order')}</a>.
                        </p>
                    </body>
                </html>
                """
            LibMail(path=path).send_mail(title=title, msg_send=msg, user_email=send_to)

        elif request.form.get('zamer_phone'):
            title="Приглашение на замер"

            msg=f"""
                <html>
                    <body>
                        <p>
                            Вам поступила заявка, клиент приглашает вас на замер.<br>Свяжитесь с клиентом по номеру:<br><a href="tel:{request.form.get('zamer_phone')}">{request.form.get('zamer_phone')}</a>.
                        </p>
                    </body>
                </html>
                """
            LibMail(path=path).send_mail(title=title, msg_send=msg, user_email=send_to)

        elif request.form.get('telephone'):
            title="Запрос консультации"

            msg=f"""
                <html>
                    <body>
                        <p>
                            Вам поступила заявка, клиент запрашивает у вас консультацию.<br> Свяжитесь с клиентом по номеру:<br><a href="tel:{request.form.get('telephone')}">{request.form.get('telephone')}</a>.
                        </p>
                    </body>
                </html>
                """
            LibMail(path=path).send_mail(title=title, msg_send=msg, user_email=send_to)

    return render_template(template_name_or_list="index.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)