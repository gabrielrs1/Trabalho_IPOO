from Produto import Produto

class Loja:
    def __iniciarLoja__(self):
        while True:
            print("\n==================================================\n")
            print("---- ESTOQUE MAIS VIRTUAL QUE VOCÊ JÁ VIU!!!---- ")
            print("\n==================================================")
            print("1 - Cadastrar produtos no Estoque.")
            print("2 - Listar todos os produtos cadastrados")
            print("3 - Remover produtos do Estoque")
            print("4 - Pesquisar produtos por preços")
            print("5 - Finalizar programa")
            print("\n=======================================")
            
            opcaoDoLogin = int(input("Digite sua opção aqui: "))
            
            if opcaoDoLogin == 1:
                print("\n=======================================")
                print("---- CADASTRO DE PRODUTO ----")
                print("=======================================")
                
                nome = input("Digite o nome: ")
                preco = float(input("Digite o preço: "))
                descricao = input("Digite a descrição: ")
                marca = input("Digite a marca: ")
                quantidade = int(input("Digite a quantidade: "))
                
                produto = Produto(nome, preco, descricao, marca, quantidade)
                produto.__cadastrarProduto__()
            
            if opcaoDoLogin == 2:
                print("\n=======================================")
                print("---- LISTAGEM DE TODOS OS PRODUTOS ----")
                print("=======================================")

                Produto.__listaProdutos__()

            if opcaoDoLogin == 3:
                print("\n=======================================")
                print("---- REMOÇÃO DE PRODUTOS ----")
                print("=======================================")
                
                nome = input("Digite o nome: ")

                Produto.__removerProduto__(nome)

            if opcaoDoLogin == 4:
                print("\n=======================================")
                print("---- LISTAR PRODUTOS POR PREÇO ----")
                print("=======================================")

                precoInicio = float(input("Preço inicial de: "))
                precoFim = float(input("Preço final até: "))

                Produto.__buscarProdutosPorPreco__(precoInicio, precoFim)

            if opcaoDoLogin == 5:
                break

loja = Loja()
loja.__iniciarLoja__()