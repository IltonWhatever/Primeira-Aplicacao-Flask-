from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Pagina Inicial - Currículo </h1><a href="/sobre">Sobre</a><br><a href="/experiencia">Experiencia</a> <br> <a href="/formacao">Formação</a> <br> <a href="/contato">Contatos</a>'

@app.route('/sobre')
def sobre():
    return '<h1>Sobre</h1><a href="/">Voltar</a> <h2>Me chamo ilton, tenho 22 anos e curso Sistemas da Informação no IFCE-Cedro.</h2>'

@app.route('/experiencia')
def experiencia():
    return '<h1>Experiencia</h1><a href="/">Voltar</a> <h2>Estagiei 4 mêses como suporte e trabalhei por 11 mêses para uma empresa de suporte a PDV</h2>'

@app.route('/formacao')
def formacao():
    return '<h1>Formação</h1> <a href="/">Voltar</a> <h2>Cursando Sistemas da Informação</h2><h2>Cusando curso de Orietação a Objeto JAVA</h2>'

@app.route('/contato')
def contato():
    return '<h1>Contatos</h1> <a href="/">Voltar</a> <h2>Email Pessoal: iltonigt@live.com</h2> <h2>Email Acadêmico: jose.ilton.silva06@aluno.ifce.edu.br</h2>'

if __name__ == '__main__':
    app.run(debug=True)