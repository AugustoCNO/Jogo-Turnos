from random import randint


class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\n Vida: {self.get_vida()}\n Nivel: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print("-="*23)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano.")
        print("-="*23)
    
    

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\n Habilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = randint(self.get_nivel() * 5, self.get_nivel() *8)
        alvo.receber_ataque(dano)
        print("-=" *35)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} e causou {dano} de dano")
        print("-="*35)


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\n Tipo: {self.get_tipo()}\n"


class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Cavaleiro", vida=100, nivel=5, habilidade="Super força")
        self.inimigo = Inimigo(nome="Morcego", vida=85, nivel=9, tipo="voador")

    def iniciar_jogo(self):
        print("-="*10)
        print("Iniciando batalha")
        print("-="*10)
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Aperte enter para atacar: ")
            escolha = input("escolha seu ataque [1] ataque normal, [2] ataque especial: ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida, escolha novamente")
            
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
        
        if self.heroi.get_vida() > 0:
            print("Parabens, você venceu a batalha")
        else:
            print("Você perdeu a batalha")

jogo = Jogo()
jogo.iniciar_jogo()
