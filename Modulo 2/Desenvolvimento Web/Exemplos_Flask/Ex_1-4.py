# EXERCICIO 1-4: Rota com número (tipagem na rota)
# Crie uma rota /dobro/<int:numero> que recebe um número e retorna o dobro dele.


from flask import Flask 




app = Flask (__name__)

@app.route('/')
def index ():
    return 'Olá mundo'

@app.route("/sobre")
def sobre ():
    return'olá,meu nome é manuele.Eu faço o curso de python'


@app.route('/saudacao/<nome>')
def saudacao (nome):
    if (nome) == 'manuele':
        return 'Mestre'
    return f'olá {nome}.Bom dia'

@app.route('/dobro/<int:numero>')
def dobro (numero):
    return f'o dobro do {numero} é {numero *2}'


if __name__ == '__main__':
    app.run(debug=True)