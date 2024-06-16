from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    # Enregistrer les informations ou les envoyer quelque part
    print(f"Nom d'utilisateur: {username}, Mot de passe: {password}")
    return "Informations reçues"

if __name__ == '__main__':
    app.run(debug=True)
