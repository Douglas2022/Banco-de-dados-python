# import mysql.connector as ms

# config = { 
#   'user': 'root', 
#   'password': '1234', 
#   'host': 'localhost', 
#   'database': 'loja', 
# }

# conexao = ms.connect(**config) 
# cursor = conexao.cursor(dictionary=True) 

# sql = 'select * from produtos'
# cursor.execute(sql)
# resposta = cursor.fetchall()

# def listar_produtos():
#     sql = 'select * from produtos'
#     cursor.execute(sql)           
#     resposta = cursor.fetchall() 
#     for resp in resposta:
#         print(f"Nome: {resp['nome']}, Preço: {resp['preco']}, QTD: {resp['quantidade']}, ID: {resp['id']}")
#     return resposta



# def atualizarQuantidade(id,quantidade):
#     sql = 'update produtos set quantidade = %s where id = %s'
#     valores = (quantidade,id)
#     cursor.execute(sql,valores)
#     conexao.commit()
    
#     print('Atualização realizada com sucesso!')

# def buscarProduto(nome):
#     sql = 'select * from produtos where nome = %s'
#     valores = (nome,)
#     cursor.execute(sql,valores)
#     resposta = cursor.fetchall()
#     for resp in resposta:
#         print(f"Id: {resp['id']}, Nome: {resp['nome']}, Preço: {resp['preco']}, Quantidade: {resp['quantidade']}")




# class Produto:
#     def __init__(self,nome,preco, quantidade):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade
#     def salvar_no_banco(self):
#         sql = 'insert into produtos (nome, preco, quantidade) values (%s,%s,%s)'
#         valores = (self.nome,self.preco,self.quantidade)
#         cursor.execute(sql,valores)
#         conexao.commit()
        
#         print('Produto Adicionado com sucesso!')

# while True:
#     opcao = input('1 - Cadastrar Produto\n2 - Listar\n3 - Atualizar Quantidade\n4 - Buscar\n5 - Sair\n')
#     if opcao == '5':
#         print('Saindo...')
#         break
#     if opcao == '1':
#         nome = input('Nome: ')
#         preco = float(input('Preço: '))
#         quantidade = int(input('Quantidade: '))

#         produto = Produto(nome,preco,quantidade)
#         produto.salvar_no_banco()
#     if opcao == '2':
#         listar_produtos()
#     if opcao == '3':
#         id = int(input('ID: '))
#         novaQuantidade = int(input('Quantidade: '))
#         atualizarQuantidade(id,novaQuantidade)
#     if opcao == '4':
#         nome = input('Nome: ')
#         buscarProduto(nome)

# i = 0
# while i <= 3:
#     i += 2
#     print("*")

# x = 1
# x = x == x
i = 0
# while i <= 3 :
#     i += 2
#     print("*")
# i = 0
# while i <= 5 :
#     i += 1
#     if i % 2 == 0:
#       break
#     print("*")
# for i in range(1):
#     print("#")
# else:
#     print("#")
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
 
# print(c + d + e)

# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])

# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]

# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
 
# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]

# nums = [1, 2, 3]
# vals = nums[-1:-2]

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)
# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)
# my_list = [i for i in range(-1, 2)]
# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
print(¡Hola Mundo!)