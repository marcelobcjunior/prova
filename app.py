from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    # Rota raiz: exibida quando o usuário acessa http://localhost:5000/
    return '''
        <h1>Sistema de Gestão</h1>
        <p>Bem-vindo ao sistema.</p>
        <a href="/index">Calculadora IMC</a> |
        <a href="/equipe">Equipe</a>
    '''

@app.route('/index')
def index():
    return render_template ('index.html')
    
    faixa = ''

    imc = (peso / (altura * altura))
    if imc < 18.5:
        faixa = 'Abaixo do peso'
    
    elif imc >= 18.5 and imc < 25:
        faixa = 'Peso normal'
    
    elif imc >= 25 and imc < 30:
        faixa = 'Sobrepeso'

    else :
        faixa = "Obeso"

    return render_template ('index.html', imc = imc, nome = nome, peso = peso, altura = altura, faixa = faixa)

    if request.method == 'GET' : 
        return render_template ('index.html')

    
    



@app.route('/equipe')
def equipe():
    return render_template ('equipe.html')


if __name__ == '__main__':
    app.run(debug=True) 