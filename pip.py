from flask import Flask, render_template, redirect, request

#inicializo o Flask
app = Flask ("Servidor")
lista_filme = ["Batman", "Barbie", "Senhor dos anéis", "O hobbit", "Era do gelo", "Shrek", "Avatar", "Homem Aranha"]
#Criar dicionario, como filmes, genero e diretores, etc...
# Defino rotas e funções
#Adcionar dicionario de filmes, com nome diretor, etc
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/filmes")
def filme():
    lista = f""
    for f in lista_filme:
        lista += f"{f}, "
    return ", ".join(lista_filme) + "."

@app.route("/ver_filmes")
def ver_filmes():
    return render_template("filmes.html", lista_filme = lista_filme)

@app.route ("/add_filme", methods =["POST"])
def add_filme():
    filme = request.form['titulo']
    if len(filme) > 3:
        lista_filme.append(filme)
    return redirect ("/ver_filmes")

@app.route("/cadastro")
def cadastro():
    return render_template("filmes")
#Rodo o Servidor

app.run(debug=True)