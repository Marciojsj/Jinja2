# Primeira coisa que temo que fazer é criar um arquivo txt (touch requirements.txt) esse arquivo vai ter todos os requerimentos que vamos ter em nossas aplicaçoes para que outra pessoa possa ter as aplicaçoes e poder instalar e executar o projeto. (pip install flask, pip freeze, pip install marcos, pip install flask-bootstrap)( se nao reconhecer o flask passar da seguinte forma pip install --target=C:\Users\marci\Documents\Pyhton-scripsts\Jinja2API flask)
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)  # Aqui estamos fazendo referência ao arquivo que estamos
bootstrap = Bootstrap(app)

itens = ["ITEM 1", "ITEM2", "ITEM3", "ITEM4"]

# Aqui podemos definir uma tela de erro, pre definido pra cada erro diferente que tiver no codigo


@app.errorhandler(404)
def not_fount_endpoint(error):
    return render_template('404.html', error=error)


# Aqui é um decorador, estamos relacionando a função com a aplicação web que recebe a URL que queremos criar, seria a raiz
@app.route("/index/")
def index():
    user_ip_information = request.remote_addr
    # função que me permite redirecionar de pagina e dentro do redirect passamos a rota que queremos ir (essa URL não existe temos que cirar abaixo criando uma nova rota)
    response = make_response(redirect("/show_information_address"))

    # com esssa resposta acima vamos criar um cookie
    response.set_cookie("user_ip_information", user_ip_information)

    return response

    # return f"Eae como ta ??, o retorno do seu IP é {user_ip_information}"


@app.route("/show_information_address")  # nova rota
def shoe_information():

    context = {
        "user_ip": user_ip,
        "itens": itens,
    }
    return render_template("ip_information.html", **context)


# Temos que definir o host (o endereço de IP) e a porta
# http://192.168.101.188:3000/index/ # Nao podemos deixar o debug True pq ele o codigo fonte, somente usar no modo desenvolvimento
app.run(host='0.0.0.0', port=3000, debug=False)
