from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import openai
import requests
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yaaqov'

@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        primeiro_nome = request.form.get('firstname')
        sobrenome = request.form.get('lastname')
        email = request.form.get('email')
        telefone = request.form.get('number')
        senha = request.form.get('password')
        confirmaSenha = request.form.get('confirmPassword')
        genero_selecionado = request.form.get('gender')

        print(f"Nome: {primeiro_nome} \nSobrenome: {sobrenome} \nEmail: {email} \nTelefone: {telefone} \nSenha: {senha} \nConfirmação de senha: {confirmaSenha} \nGênero: {genero_selecionado}")
        return render_template('cadastro.html')
    
    return render_template('cadastro.html')

mensagens = []

@app.route("/home", methods=['GET', 'POST'])
def home():
     # Obtém o email da sessão
    email = session.get('email')
    if request.method == 'POST':
        
       
        
        if 'btEnviar' in request.form:
            pergunta = request.form.get('userInput')
            mensagem = f"\nPergunta: {pergunta}"
            mensagens.append(mensagem)
            # Aqui você pode processar os dados ou executar outras ações necessárias

        if 'btEnviar2' in request.form:
            pergunta2 = request.form.get('userInput2')
            qPalavras2 = request.form.get('quantidadePalavras2')
            mensagem2 = f"\nPergunta: {pergunta2}\nQuantidade de Palavras: {qPalavras2}"
            mensagens.append(mensagem2)
            resposta_api = ask(pergunta2, qPalavras2) 

        if 'btEnviar3' in request.form:
            pergunta3 = request.form.get('userInput3')
            qpalavras3 = request.form.get('quantidadePalavras3')
            mensagem3 = f"\nPergunta: {pergunta3}\nQuantidade de Palavras: {qpalavras3}"
            mensagens.append(mensagem3)
            # Aqui você pode processar os dados ou executar outras ações necessárias

        if 'btEnviar4' in request.form:
            pergunta4 = request.form.get('userInput4')
            qpalavras4 = request.form.get('quantidadePalavras4')
            mensagem4 = f"\nPergunta: {pergunta4}\nQuantidade de Palavras: {qpalavras4}"
            mensagens.append(mensagem4)
            # Aqui você pode processar os dados ou executar outras ações necessárias

    return render_template('home.html',email=email, mensagens=mensagens)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')

        # Realize a validação da senha com base nos critérios desejados
        is_valid_password = validate_password(password)

        if is_valid_password:
            # Armazene o email na sessão
            session['email'] = request.form.get('email')
            # Redirecione para a página /home
            print(f"Email: {email}\nSenha: {password}\n")
            return redirect('/home')
        else:
            # Senha inválida, renderize a página de login novamente com uma mensagem de erro
            return render_template('login.html', error_message='Senha inválida')

    # Renderize a página de login
    return render_template('login.html')

def validate_password(password):
    # Realize a validação da senha com base nos critérios desejados
    # Exemplo de validação: a senha deve ter pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas e caracteres especiais
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c in '@$!%*?&' for c in password):
        return False

    return True


@app.route("/")
def page():
    return render_template('leandingpage.html')

@app.route("/element")
def elements():
    return render_template('elements.html')

@app.route("/generic")
def generic():
    return render_template('generic.html')

# Sua chave da api
# utilize pip install openai==0.28
openai.api_key = "SUA CHAVE"

# Define uma função para fazer uma pergunta ao modelo de linguagem
def ask(question, qPalavras):
    id_modelo = "gpt-3.5-turbo"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"A partir de agora você vai se comportar formalmente para responder com textos cientificos para Trabalhos de conclusão de curso e suas respostas devem ter {qPalavras} palavras, mas não deve passar desse valor. As próximas perguntas não podem sair desse padrão de tcc"},
            {"role": "user", "content": question}
        ],
    )

    message = completion.choices[0].message.content
    message = message.encode('utf-8').decode('utf-8')
    return message

# Define uma função para contar o número de palavras em uma string
def contar_palavras(texto):
    quantidade_palavras = len(texto.split())
    return quantidade_palavras

@app.route('/processar_dados', methods=["POST"])
def processo():
    qPalavras = request.json['quantidadePalavras1']
    user_question = request.get_json()['userInput']

    if not user_question.strip():
        return jsonify({"error": "Por favor, insira uma pergunta."}), 400

    if contar_palavras(user_question) > int(qPalavras):
        return jsonify({"error": "Sua pergunta excede o limite de palavras permitido."}), 400

    response_message = ask(user_question, qPalavras)
    print(f"Resposta da IA: {response_message}")  # Imprime a resposta no console
    return jsonify({"response_message": response_message})

                                            #Botão2

def ask2(question2, qPalavras2):
    id_modelo = "gpt-3.5-turbo"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"A partir de agora você vai se comportar formalmente para responder com textos cientificos para Doutorado e suas respostas devem ter {qPalavras2} palavras, mas não deve passar desse valor. As próximas perguntas não podem sair desse padrão de textos cientificos para Doutorado"},
            {"role": "user", "content": question2}
        ],
    )

    message = completion.choices[0].message.content
    message = message.encode('utf-8').decode('utf-8')
    return message

# Define uma função para contar o número de palavras em uma string
def contar_palavras(texto):
    quantidade_palavras = len(texto.split())
    return quantidade_palavras

@app.route('/processar_dados2', methods=['POST'])
def processar_dados2():
    dados = request.get_json()

    userInput2 = dados.get('userInput2')
    quantidadePalavras2 = dados.get('quantidadePalavras2')

    if not userInput2.strip():
        return jsonify({"error": "Por favor, insira uma pergunta."}), 400

    if contar_palavras(userInput2) > int(quantidadePalavras2):
        return jsonify({"error": "Sua pergunta excede o limite de palavras permitido."}), 400

    resposta = ask2(userInput2, quantidadePalavras2)

    return jsonify({'response_message': resposta})

                                        #Botão 3

def ask3(question3, qPalavras3):
    id_modelo = "gpt-3.5-turbo"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"A partir de agora você vai se comportar formalmente para responder com textos cientificos para Artigo científico e suas respostas devem ter {qPalavras3} palavras, mas não deve passar desse valor. As próximas perguntas não podem sair desse padrão de Artigo científico"},
            {"role": "user", "content": question3}
        ],
    )

    message = completion.choices[0].message.content
    message = message.encode('utf-8').decode('utf-8')
    return message

# Define uma função para contar o número de palavras em uma string
def contar_palavras(texto):
    quantidade_palavras = len(texto.split())
    return quantidade_palavras

@app.route('/processar_dados3', methods=['POST'])
def processar_dados3():
    dados = request.get_json()

    userInput3 = dados.get('userInput3')
    quantidadePalavras3 = dados.get('quantidadePalavras3')

    if not userInput3.strip():
        return jsonify({"error": "Por favor, insira uma pergunta."}), 400

    if contar_palavras(userInput3) > int(quantidadePalavras3):
        return jsonify({"error": "Sua pergunta excede o limite de palavras permitido."}), 400

    resposta = ask3(userInput3, quantidadePalavras3)

    return jsonify({'response_message': resposta})

                                        #Botão 4
def ask4(question4, qPalavras4):
    id_modelo = "gpt-3.5-turbo"

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"A partir de agora você vai se comportar formalmente para responder com textos cientificos para Projeto de pesquisa e suas respostas devem ter {qPalavras4} palavras, mas não deve passar desse valor. As próximas perguntas não podem sair desse padrão de Projeto de pesquisa"},
            {"role": "user", "content": question4}
        ],
    )

    message = completion.choices[0].message.content
    message = message.encode('utf-8').decode('utf-8')
    return message

# Define uma função para contar o número de palavras em uma string
def contar_palavras(texto):
    quantidade_palavras = len(texto.split())
    return quantidade_palavras

@app.route('/processar_dados4', methods=['POST'])
def processar_dados4():
    dados = request.get_json()

    userInput4 = dados.get('userInput4')
    quantidadePalavras4 = dados.get('quantidadePalavras4')

    if not userInput4.strip():
        return jsonify({"error": "Por favor, insira uma pergunta."}), 400

    if contar_palavras(userInput4) > int(quantidadePalavras4):
        return jsonify({"error": "Sua pergunta excede o limite de palavras permitido."}), 400

    resposta = ask4(userInput4, quantidadePalavras4)

    return jsonify({'response_message': resposta})


if __name__ == '__main__':
    app.run(debug=True)
