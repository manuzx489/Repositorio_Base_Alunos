# EXERCICIO 1-3: Parâmetros na URL (rotas dinâmicas)
# Crie uma rota /saudacao/<nome> que retorna "Olá, <nome>! Seja bem-vindo!".


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


if __name__ == '__main__':
    app.run(debug=True)
