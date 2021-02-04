from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from json import load
from lib.mail import LibMail


app = Flask(__name__)
path = "/home/cosmobot/apartment_renovation/"
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