# EXERCICIO 1-2: Rota personalizada
# Adicione uma nova rota /sobre que retorna uma mensagem com seu nome e uma frase sobre você.


from flask import Flask 




app = Flask (__name__)

@app.route('/')
def index ():
    return 'Olá mundo'

@app.route("/sobre")
def sobre ():
    return'olá,meu nome é manuele.Eu faço o curso de python'

if __name__ == '__main__':
    app.run(debug=True)
