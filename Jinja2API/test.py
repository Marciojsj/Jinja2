import jinja2

# aqui estou guardando meu template
model = 'Olá {{ nome }}, seja bem vindo, seu email é: {{ email}} e seu estado: {{estado}} '

# lista com os campos

dados = [["teste2@gmail.com", "Marcio Junior", "3São Paulo"],
         ["teste3@gmail.com", "Marcio Junior", "4São Paulo"],
         ["teste4@gmail.com", "Marcio Junior", "5São Paulo"],
         ]

# Primeiro vamos carregar o template para a variavel

template = jinja2.Template(model)  # Aqui carregamos nosso tamplate

# agora eu quero gerar um template diferente apartir deste modelo atras de um for
# e renderizar ( renderizar geralmente se refere ao processo de combinar um template)

for element in dados:
    email, nome, estado = element
    print(template.render(nome=nome, email=email, estado=estado))
