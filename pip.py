from flask import Flask, render_template

#inicializo o Flask
app = Flask ("Servidor")
testes = ["Batman", "Barbie", "Senhor dos anéis", "O hobbit", "Era do gelo", "Shrek"]
#Criar dicionario, como filmes, genero e diretores, etc...
# Defino rotas e funções
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/teste")
def teste():
    lista = f""
    for f in testes:
        lista += f"{f}, "
    return lista

#Rodo o Servidor

app.run(debug=True)