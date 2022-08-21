list = []

# Função para verificar quais usuários estão na faixa etária
def category(inicial,final):
    filtered = []
    # Laço para percorrer a lista e pegar o nome (posição 0) e a idade (posição 1)
    for i in list:
        name = i[0]
        age = i[1]
        # Condição da categoria etária
        if(age > inicial and age <= final):
            # Adiciona a pessoa à lista filtrada da categoria
            filtered.append(name)
        else:
            pass
    # Se não houver ninguém que atenda às condições da categoria, a lista filtrada estará vazia.
    if(filtered == []):
        # Imprimir mensagem de que não há pessoas nessa faixa etária.
        print("\n Não há pessoas nessa faixa etária.")
    # Se houver pessoas, imprimir elas.
    else:
        for i in filtered:
            print(i)

while True:
    option = input('''
    =========================== MENU =============================
    ==============================================================
    [1] - NOVO CADASTRO                                           
    [2] - LISTA DE PESSOAS CADASTRADAS
    [3] - LISTA DE PESSOAS CADASTRADAS - ORDENAR POR IDADE
    [4] - LISTA DE PESSOAS CADASTRADAS - ORDENAR DE A a Z
    [5] - LISTA DE PESSOAS CADASTRADAS - FILTRAR POR CATEGORIAS
    [6] - SAIR DO PROGRAMA
    ============================================================== 

    Digite o número da opção desejada e tecle [ENTER] para confirmar: '''

    )

    # Caso o usuário escolha a opção 1:
    if option == '1':
        while True:
            data = []
            print("\n================ NOVO CADASTRO ================")
            # Input para cadastrar o nome do usuário. Método "upper()" utilizado para transformar todas as letras em maiúsculas.
            name = input("Para voltar para a página principal, digite [SAIR]\nNOME: ").upper()
            # Caso o usuário deseje voltar para a página principal, basta digitar [SAIR].
            if name == 'SAIR':
                print("Etapa de cadastros finalizada com sucesso.")
                break
            else:
                pass
            while True:
                # Tratamento de erros com try/except, caso o usuário não digite um número inteiro.
                try:
                    age = int(input("IDADE: "))
                    break
                except:
                    print('Utilize apenas números inteiros.')
            # Se tudo estiver ok, o programa registrará o nome e a idade na lista.
            data.append(name)
            data.append(age)
            # Adicionando a lista "data" dentro da lista "list".
            list.append(data)

    # Caso o usuário escolha a opção 2
    elif option == '2':
        print("======== LISTA DE PESSOAS CADASTRADAS (NOME - IDADE) ========")
        # Laço para percorrer a lista de pessoas cadastradas.
        for i in list:
            # Imprime as pessoas cadastradas e a idade pelo index do elemento.
            print(i[0],"  -  ",i[1])

    # Caso o usuário escolha a opção 3
    elif option == '3':
        # Criação de uma lista para ordenamento, para não alterar a lista original.
        ordered_list = []
        print("======== LISTA DE PESSOAS CADASTRADAS (ORDENADA POR IDADE) ========")
        # Utilização da função sorted para ordenação a partir do indice [1] das listas.
        ordered_list = sorted(list,key=lambda x:x[1])
        # Laço para passar por cada um dos elementos e imprimi-los.
        for i in ordered_list:
            print(i[0],"  -  ",i[1])

    # Caso o usuário escolha a opção 4
    elif option == '4':
        print("======== LISTA DE PESSOAS CADASTRADAS (EM ORDEM ALFABÉTICA) ========")
        # Ordenação de A a Z utilizando o método sort, visto que essa lista foi criada apenas para ordenação.
        ordered_list.sort()
        # Laço para passar por cada um dos elementos e imprimi-los.
        for i in ordered_list:
            print(i[0],"  -  ",i[1])

    # Caso o usuário escolha a opção 5
    elif option == '5':
        while True:
            # Tratamento de erro com o try/except
            try:
                selection = input('''
                
                DESEJA FILTRAR POR QUAL CATEGORIA?
            
                [1] - MOSTRAR APENAS CRIANÇAS
                [2] - MOSTRAR APENAS ADOLESCENTES
                [3] - MOSTRAR APENAS ADULTOS
                [4] - MOSTRAR APENAS IDOSOS
                [5] - VOLTAR
                
                ESCOLHA: ''')

                # Caso o usuário escolha a seleção 1, o programa mostrará as crianças cadastradas.
                if (selection == '1'):
                    print("\n==== LISTA DE CRIANÇAS ====")
                    # Função que possui como parâmetros 0 e 12 (idades para filtro).
                    category(0,12)
                # Caso o usuário escolha a seleção 2, o programa mostrará os adolescentes cadastrados.
                elif (selection == '2'):
                    print("\n==== LISTA DE ADOLESCENTES ====")
                    # Função que possui como parâmetros 12 e 19 (idades para filtro).
                    category(12, 19)
                # Caso o usuário escolha a seleção 3, o programa mostrará os adultos cadastrados.
                elif (selection == '3'):
                    print("\n==== LISTA DE ADULTOS ====")
                    # Função que possui como parâmetros 19 e 65 (idades para filtro).
                    category(19,65)
                # Caso o usuário escolha a seleção 4, o programa mostrará os idosos cadastrados.
                elif (selection == '4'):
                    print("\n==== LISTA DE IDOSOS ====")
                    # Função que possui como parâmetros 65 e 110 (idades para filtro).
                    category(65,110)
                # Caso o usuário escolha a seleção 5, volta para o menu principal.
                elif (selection == '5'):
                    break
                # Caso o usuário digite uma opção inválida.
                else:
                    print("\nESCOLHA UMA OPÇÃO VÁLIDA.")
            except:
                print("\nESCOLHA UMA OPÇÃO VÁLIDA.")

    # Caso o usuário escolha a opção 6, o programa finaliza.
    elif option == '6':
        print("\nOBRIGADO POR UTILIZAR O SISTEMA DE CADASTRO E-CORE.")
        break

    # Caso o usuário escolha uma opção inválida no menu principal.
    else:
        print("\nESCOLHA UMA OPÇÃO VÁLIDA NO MENU!")


