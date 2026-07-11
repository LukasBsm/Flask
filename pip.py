from flask import Flask, render_template

#inicializo o Flask
app = Flask ("Servidor")

# Defino rotas e funções
@app.route("/")
def homepage():
    return render_template("index.html")

#Rodo o Servidor

app.run(debug=True)