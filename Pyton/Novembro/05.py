class produtos:

    def __init__(self, nome, preco, quantidade):
        self.nome= nome
        self.preco= preco
        self.quantidade= quantidade
    
    def mostrar_info(self):
        print(f"{self.nome} | R$ {self.preco} | {self.quantidade} un ")
    
    def valor_do_estoque(self):
        valor_do_estque= self.preco*self.quantidade
        print(f"O total de estoque do {self.nome} e de R$ {valor_do_estque}")

produto1= produtos("Macarrao", 11.99, 25)
produto1.mostrar_info()
produto1.valor_do_estoque()

print(20*"-")

produto2= produtos("Vassoura", 14.99, 10)
produto2.mostrar_info()
produto2.valor_do_estoque()