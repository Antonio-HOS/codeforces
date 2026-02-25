# ta faltando conluir o teste 10

count = 0
 
class Node:
    def __init__(self, alutra, largura, posicao):
            self.largura = largura
            self.altura = alutra
            self.next = None
            self.posicao = posicao
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, altura, largura, alturaC, larguraC, posicao):
        global count
        if(altura<=alturaC or largura <=larguraC):
            print("[envelope menor que o cartao]")
            return
        new_node = Node(altura, largura, posicao)
 
        if not self.head:
            self.head = new_node
            print("[não existe head]")
            count +=1
            return
        
        last = self.head
 
        if not(last.altura <= new_node.altura and last.largura <= new_node.largura ):
            self.head = new_node
            new_node.next=last
            count +=1
            print("[altura do head nao atual não é a menor possivel]")
            return
        
        while last.next:
            current = last.next
            print("[passando pelo laco]")
 
            if(last.altura == new_node.altura or last.largura == new_node.largura):
                print("[tamanho de envelope igual a ja existente]")
                return
            
            if(current.altura > new_node.altura and current.largura > new_node.largura):
               
                last.next = new_node
                new_node.next = current                
                count +=1 
                print("[caminhado com ponteiro em direcao ao fim da lista]")
                return    

 
            else:
                last = last.next
                print("[adicionando novo no]")
 
        if not(last.altura == new_node.altura or last.largura == new_node.largura):
            print("[fugio de todas as condicoes]")
            count +=1
            last.next=new_node
 
 
    def print(self):
        current = self.head
        if not count:
            return
        while current:
            print(current.posicao, end= ' ' )
 
            current = current.next
 
 
 
entrada = input().split()
qntd_cartoes= int(entrada[0])
altura_cartao= int(entrada[1])
largura_cartao= int(entrada[2])
 
envelopes = LinkedList()
 
 
posicao = 0
 
for i in range(qntd_cartoes):
    new_envelope = input().split()
    posicao += 1
    envelopes.insert(int(new_envelope[0]), int(new_envelope[1]), altura_cartao, largura_cartao, posicao)
 
print(count)
envelopes.print()
