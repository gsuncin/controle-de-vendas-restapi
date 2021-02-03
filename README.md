# Controle de Vendas
Plataforma de controle de vendas

Desenvolvido em Python + Django, foi utilizado tanto o framework Django RestFramework quanto o python puro para 
serializar e devolver JsonResponses

Versão do Python -> 3.8

Doc Postman: https://documenter.getpostman.com/view/14447105/TW71n7LA

# Instruções:
- <strong>Criar um ambiente virtual com Python-3.8 e instale todos os requirements do Projeto "requirements.txt"</strong> 

- <strong>Backup do Banco (sqlite) no diretório raiz</strong>
      
- <strong>Importe todas as coleções do Postman:</strong>
            => "controle-vendas.postman_collection.json"

- <strong>Necessário realizar login para realizar um request.</strong>
      Dados:
          usuário: "dev", 
          senha: "P1!2DyceH#oS"
 
- <strong>Utilize as requisições do Postman:</strong>
        Utilize todos os testes da Collection através dos endpoints criados
  
Obs. Todos os exemplos de requisições estão salvas na cópia 'exportada' do Postman na raíz do projeto
  
# EndPoints


- Produtos

Listar produtos -> http://127.0.0.1:8000/list-produtos/ - GET listar todos os produtos
--- Retorna um Json com todos os Produtos


Listar produtos + filtro -> http://127.0.0.1:8000/list-produtos/?nome=xxxx&valor=yyyy - get listar todos os produtos com filtro
--- Retorna um Json com todos os Produtos


Detalhar produto -> http://127.0.0.1:8000/detail-produtos/1 - GET visualizar detalhes do produto
--- Retorna um Json com todos os dados do Produto buscado


Adicionar Produto -> http://127.0.0.1:8000/add-produtos/ - POST adicionar produtos ---
 exemplo:

        {'identificador': Numero do identificador do Produto, 
        'nome': Nome do Produto, 
        'numero_lote': numero Identificador do Lote do Produto,
        'valor': caso precise de um numero com casas decimais, utilizar o ponto pra separá-las, 
        'cor': nome da cor, 
        'descricao':Descrição do produto}

- Pedidos

Listar pedidos -> http://127.0.0.1:8000/list-pedidos/ - GET visualizar todos os pedidos
--- Retorna um Json com todos os Pedidos

Listar produtos + filtro -> http://127.0.0.1:8000/list-pedidos/?valor_total=xxxx&data_compra=yyyy
- GET listar todos os pedidos com filtro
--- Retorna um Json com todos os Pedidos

Detalhar Pedido -> http://127.0.0.1:8000/detail-pedidos/1 - GET visualizar detalhes do pedido
--- Retorna um Json com todos os dados do Pedido buscado

Adicionar Pedido -> http://127.0.0.1:8000/add-pedidos/ - POST adicionar pedidos ---
exemplo:

        {'identificador': Numero do identificador do Pedido, 
        'produtos': Numero de Identificação dos Produtos (separar por espaços em branco, ex: '12 1952'), 
        'status': numero do status, Ativo = 1; Pendente = 2; Concluido = 3; Cancelado = 4,
        'cliente': Nome completo do Cliente cadastrado no sistema, 
        'cor': nome da cor, 
        'vendedor': Utilizar o username do vendedor cadastrado,
        'valor_total': caso precise de um numero com casas decimais, utilizar o ponto para separá-las}

- Lotes

Listar lotes -> http://127.0.0.1:8000/list-lotes/ - GET visualizar todos os lotes 
--- Retorna um Json com todos os Lotes

Detalhar Lote -> http://127.0.0.1:8000/detail-lotes/1 - GET visualizar detalhes do lote
--- Retorna um Json com todos os dados do Lote buscado


- Clientes

Listar clientes -> http://127.0.0.1:8000/list-clientes/ - GET visualizar todos os lotes 
--- Retorna um Json com todos os Clientes

Detalhar cliente -> http://127.0.0.1:8000/detail-clientes/1 - GET visualizar detalhes do lote
--- Retorna um Json com todos os dados do Cliente buscado

- Auth

path('login/', api_login, name='login'),
path('logout/', auth_views.logout_then_login, name='logout'),



Desenvolvido por: Gabriel Suncin - 12/2020
