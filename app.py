from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    if request.method == 'POST':
        nome = request.form.get ('nome')
        peso = request.form.get ('peso')
        altura = request.form.get ('altura') 
        
        nome = nome
        peso = float(peso)
        altura = float(altura)

        erros = []
        if not nome:
            erros.append('Nome obrigatório')
        elif len(nome) < 3:
            erros.append('Mínimo 3 caracteres.')
        
        if not peso:
            erros.append('Peso obrigatório')
        if peso <= 0:
            erros.append('Peso tem que ser maior que 0')

        if not altura:
            erros.append('Altura obrigatória')
        if altura < 0.5 and altura > 2.5:
            erros.append('Altura precisa ser entre 0,5 e 2,5')

        if erros: 
            for erros in erros :
                flash(erro, 'danger')

        return render_template ('index.html', erros = erros)

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