import os

def limpar_tela():
    #vai detectar o sistema operacional e usa o comando correto
    if os.name == 'nt':  #'nt' é para Windows
        os.system('cls')
    else:
        # pro Linux e Mac
        os.system('clear')

def menu():
    limpar_tela()  # limpa a tela antes de mostrar o menu principal
    print("""    ==============================================
    Loja de Roupas Online
    ==============================================
    Insira a seguir as opções que você deseja:
    1 - Ver catálogo
    2 - Pesquisar Peças
    3 - Ver melhores preços
    0 - Se deseja sair
    ==============================================
    4 - Opções de Administrador
    ==============================================""")
#função para exibir o menu principal

def login():
    limpar_tela() #limpa a tela antes de mostrar o login
    print('''==============================================
        Digite a senha de administrador:
==============================================    
 ''')
    senha = 2810
    senhainformada = 1
    while senha != senhainformada:
        senhainformada = int(input("Digite a senha de adm: "))
        
        if senha == senhainformada:
            menuadm()
            return
        print("Senha incorreta!")
        senhaincorreta = input("Deseja tentar novamente? (s/n) ").upper()
        
        if senhaincorreta == 'N':
            break

def menuadm():
    limpar_tela()  #limpa a tela antes de mostrar o menu do administrador
    print("""    ==============================================
    Opções de Administrador
    ==============================================
    1 - Inserir itens dentro de uma categoria
    2 - Remover item de determinada categoria
    ==============================================
    3 - Sair do menu ADM
    ==============================================      """)
    opcaoselecionada = int(input("Digite a opção que deseja selecionar: "))
    
    if opcaoselecionada == 1: 
        #inserir os itens em determinada categoria
        true = True
        while true:  #loop para inserir múltiplos itens
            selecionar_categorias()
            categoria_escolhida = int(input("Digite a categoria que deseja inserir os itens: "))
            
            #escolhe a categoria
            if categoria_escolhida == 1:
                nomeitemadicionado = input("Digite o nome da peça que deseja inserir: ").upper()
                precoitemadicionado = float(input("Digite o preço da peça que deseja inserir: "))
                catalogo[0][nomeitemadicionado] = precoitemadicionado
            
            elif categoria_escolhida == 2:
                nomeitemadicionado = input("Digite o nome da peça que deseja inserir: ").upper()
                precoitemadicionado = float(input("Digite o preço da peça que deseja inserir: "))
                catalogo[1][nomeitemadicionado] = precoitemadicionado
            
            elif categoria_escolhida == 3:
                nomeitemadicionado = input("Digite o nome da peça que deseja inserir: ").upper()
                precoitemadicionado = float(input("Digite o preço da peça que deseja inserir: "))
                catalogo[2][nomeitemadicionado] = precoitemadicionado
            
            else:
                print("Opção indefinida, tente novamente")
                continue  #retorna ao início do loop
            
            #pergunta se o usuário deseja adicionar mais itens
            continuar_inserindo = input("Deseja inserir mais itens? (s/n): ").upper()
            if continuar_inserindo != 'S':
                break  # Sai do loop se o usuário não quiser adicionar mais itens

        #mostra o catálogo atualizado sem colchetes ou chaves
        mostrar_catalogo(catalogo)
        input("Digite enter para voltar ao menu")
    
    elif opcaoselecionada == 2:
        #remover itens de uma determidada categoria
        continuar_removendo = 'S'
        while continuar_removendo == 'S':
            mostrar_catalogo(catalogo)
            #mostra o catalogo pro usuario para que ele possa visualizar as peças que ele deseja remover
            itemremovido = input("Digite o nome da peça que deseja remover: ").upper()
            
            item_encontrado = False  #flag para verificar se o item foi encontrado
            for categoria in catalogo:
                if itemremovido in categoria:
                    del categoria[itemremovido]
                    print(f"{itemremovido} foi removido com sucesso.")
                    item_encontrado = True
                    break
            
            if not item_encontrado:
                print("Item não encontrado.")
            
            continuar_removendo = input("Deseja remover outro item? (s/n): ").upper()
        
        print("Aqui está o catálogo atualizado:")
        mostrar_catalogo(catalogo)
        #a partir daqui irá mostrar todo o catálogo atualizado, ja com a(s) remoções
        input("Digite enter para voltar ao menu")
        
    elif opcaoselecionada == 3:
        print("Voltando ao menu...")
        return
    
    else:
        print("Opção indefinida, tente novamente")
        menuadm()

def selecionar_categorias():
    print("""Categorias para selecionar:
                  1 - Camisetas
                  2 - Calças
                  3 - Bermudas""")
#função para exibir as categorias disponíveis

def mostrar_catalogo(lista: list):
    for valor in lista:
        print(barras)
        for itens, preco in valor.items():
            print(f"{itens}: R$ {preco:.2f}")
#função para exibir o catálogo de forma organizada e sem colchetes/chaves

def verificar_itens(item: str):
    for categoria in catalogo:
        if item in categoria:
            return categoria, item, True
    return None, None, False
#função para verificar se o item está no catálogo

def reservar_itens(item):
    categoria, nome_item, achou = verificar_itens(item)
    if achou:
        pecas_reservadas.append((nome_item, categoria[nome_item]))
    else:
        print("Produto não encontrado")
#função para adicionar itens à lista de reservas

def calcular_total_reservas():
    total = 0 #inicializa o total como zero
    
    for _, preco in pecas_reservadas: #percorre a lista de peças reservadas
        total += preco #adiciona o preço de cada peça ao total
    return total #retorna o total calculado
#função que soma o valor das peças reservadas. isso tudo só pra não usar a "sum".

def exibir_reservas():
    print("Você reservou as seguintes peças:")
    for nome_item, preco in pecas_reservadas:
        print(f"{nome_item}: R$ {preco:.2f}")
#função para exibir as peças reservadas

barras = str("==============================================")
#meramente estético para fazer um print mais bonito

camisetas = {   
    "CAMISETA AZUL": 39.90,
    "CAMISETA PRETA": 49.90,
    "CAMISETA MARROM": 42.90,
    "CAMISETA BRANCA": 49.90,
}

bermudas = {   
    "BERMUDA AZUL": 39.90,
    "BERMUDA PRETA": 49.90,
    "BERMUDA BRANCA": 49.90,
    "BERMUDA MARROM": 59.90
}

calcas = {
    "CALÇA JEANS PRETA": 149.90,
    "CALÇA JEANS BÁSICA": 99.90,
    "CALÇA MOLETOM PRETA": 72.80,
    "CALÇA MOLETOM BRANCA": 72.80
}

catalogo = [camisetas, bermudas, calcas]
#lista onde tem armazenado as três categorias de roupa que foram feitas a partir de dicionários

pecas_reservadas = []
#aqui vao ser armazenadas as peças que vão ser reservadas pelo usuário. dessa forma é mais facil de usar os itens escolhidos

opcao = 1
#loop para executar até o usuário optar por sair
while opcao != 0: 
    menu()

    opcao = int(input("Digite a opção que deseja selecionar: "))
    #input para selecionar a opção que é dada pelo menu

    while opcao < 0 or opcao > 4:
        opcao = int(input("Opção Indefinida, tente novamente: "))
    
    if opcao == 1:
        mostrar_catalogo(catalogo)
        #mostra todo o catálogo registrado
        print(barras)
        #meramente estético

        opcao_catalogo = input("Deseja reservar algum item?(s/n): ").upper()
        while opcao_catalogo == "S":
            opcao_catalogo_mais = str(input("Digite o nome da peça: ")).upper()
            reservar_itens(opcao_catalogo_mais)
            opcao_catalogo = input("Deseja reservar mais algum item?(s/n): ").upper()
        
        if pecas_reservadas:
            exibir_reservas()
            total = calcular_total_reservas()
            print(f"O valor total das suas reservas é: R$ {total:.2f}")
        else:
            print("Você não reservou itens.")
        
        input("Aperte enter para voltar para o menu")
    
    elif opcao == 2:
        #função de pesquisa de peças
        continuar_pesquisando = 'S'
        while continuar_pesquisando == 'S':
            pesquisa = str(input("Digite o nome da peça que deseja pesquisar: ")).upper()
            categoria, nome_item, achou = verificar_itens(pesquisa)
            #usa a def verificar_itens para conseguir ver se a peça realmente está registrada e conseguir saber se deve-se falar ao usuário se a peça foi encontrada ou se ela nao existe no catalogo
            
            if achou:
                print(f"Peça encontrada: {nome_item}, Preço: {categoria[nome_item]}")
            else:
                print("Peça não encontrada.")
            
            continuar_pesquisando = input("Deseja fazer outra pesquisa? (s/n): ").upper()
        
        input("Aperte enter para voltar ao menu")
    
    elif opcao == 3:
        #mostrar 5 peças com os menores preços
        precos = []
        for categoria in catalogo:
            precos.extend(list(categoria.items()))
        
        precos.sort(key=lambda x: x[1])
        menores_precos = precos[:5]
        print("As 5 peças com os menores preços são:")
        
        for item in menores_precos:
            print(f"{item[0]}: R$ {item[1]:.2f}")
        input("Aperte enter para voltar ao menu")

    elif opcao == 0:
        #fecha a loja
        print("Obrigado por acessar nosso site")

    elif opcao == 4:
        #abre o menu de adm
        #a senha é 2810!
        login()
        #a função irá trazer todo o menu de login e logo apos isso também irá executar o codigo que da as opções para o usuário (adm) escolher o que deseja fazer.
        #toda o codigo do adm ocorre dentro de funções, por isso esse elif ficou tão solitário :(