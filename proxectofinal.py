from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para almacenar los textos informativos
textos = []

@app.route('/')
def index():
    return render_template('index.html', textos=textos)

@app.route('/agregar', methods=['POST'])
def agregar_texto():
    texto = request.form['texto']
    textos.append(texto)
    return render_template('index.html', textos=textos)

if __name__ == '__main__':
    app.run(debug=True)


