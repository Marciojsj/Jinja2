# Carregando um template de um projeto externo, para isso vamos criar uma pasta no projeto e carregar os arquivos HTML dentro desta pasta, depois de criarmos a pasta com os templates e suas variveis vamos fazer os imports

from jinja2 import FileSystemLoader, Environment

# primeiro vamos criar a variavel loader que vai receber a classse FileSystemLoader, essa pasta carrega os arquivos da pasta aonde estaram os templates e como parametro vamos passar o nome da pasta diretorio dos arquivos

loader = FileSystemLoader('templates')

# Vamos criar a variavel env que vai receber Environment e criar nosso ambiente e temos que passar o parametro (loader=) que foi a variavel que definimos logo acima 

env = Environment(loader=loader)

# agora vamos carregar o nosso template que vai receber nosso ambiente e como parametro passamos o arquivo que esta dentro da pasta (template)

template = env.get_template('template.html')

# agora que ja temos o template precisamos rederizar o template

render = template.render(titulo="Teste com jinja", cor_fundo="#000", cor_texto="#FFF", nome="Marcio Junior")

# Agora esse escript vai gerar um arquivo HTML deste template, pra isso temos que criar uma nova pasta (output) aonde vai salvar esse arquivo. temos que passar o nome da pasta a ser salva e o nome do arquivo que vai se gerar, o 'w' da a permissao de escrita *?*

file = open('output/index.html', 'w')

# o file.whire permite que escrever dentro do arquivo nossa redenrização e por fim fechar o file

file.write(render)
file.close()
