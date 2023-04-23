import boto3
import random
import datetime
from credential import tabela_produtos

# Cria conexão com AWS Dynamodb
boto3.setup_default_session(profile_name="default")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(tabela_produtos)

opcoes_pagamento = ["pix", "debito", "credito", "boleto"]

produtos = [
    "Tênis de corrida Nike",
    "Relógio inteligente Apple Watch",
    "Câmera DSLR Canon",
    "Fone de ouvido sem fio Bose",
    "Cafeteira elétrica Nespresso",
    "Console de jogos Xbox Series X",
    "Smart TV Samsung de 55 polegadas",
    "Guitarra elétrica Fender Stratocaster",
    "Aspirador de pó Robô Roomba",
    "Mochila de viagem de couro",
    "Mesa de escritório em madeira maciça",
    "Kit de ferramentas Bosch",
    "Drone DJI Phantom",
    "Livro de receitas vegetarianas",
    "Jogo de tabuleiro Catan",
    "Máquina de cortar cabelo Wahl",
    "Cafeteira italiana Bialetti",
    "Tênis de basquete Adidas",
    "Teclado mecânico RGB Corsair",
    "Impressora multifuncional HP"
]

purchases = [
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
    {
        "tipo_produto": "Itens Marketplace",
        "nome_produto": random.choice(produtos),
        "preco": "R${:,.2f}".format(random.uniform(0, 9.99) if random.random() < 0.5 else random.uniform(10, 999.99)),
        "data_hora": f"{datetime.datetime.now().strftime('%d')}/{datetime.datetime.now().strftime('%m')} - {datetime.datetime.now().strftime('%H:%M:%S')}",
        "ano": datetime.datetime.now().strftime("%Y"),
        "forma_pagamento": random.choice(opcoes_pagamento),
    },
]

# exemplo de estrutura do item:
'''
{
    'tipo_produto': 'Itens Marketplace', 
    'nome_produto': 'Mochila de viagem de couro', 
    'preco': 'R$95.73', 'data_hora': '23/04 - 19:10:30', 
    'ano': '2023', 
    'forma_pagamento': 'pix'}
'''
for purchase in purchases:
    purchases.pop(purchases.index(purchase))
    print(purchase)
    table.put_item(Item=purchase)
