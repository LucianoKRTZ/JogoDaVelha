
import tkinter as tk
import random
import time



class Main():
    def __init__(self):
        self.root = None
        self.tagUser = 'X'
        self.tagComputer = 'O'

        self.placarComputer = None
        self.placarUser = None
        self.pontosComputer = 0
        self.pontosUser = 0

        pass

    def iniciarTela(self):
        self.root = tk.Tk()
        self.root.title("Jogo da Velha")
        tk.Label(self.root, text="Jogo da Velha", font=("Arial", 24)).grid(row=0, column=0, columnspan=3, pady=10)
        self.root.geometry("317x500")

        self.botoes = []
        for i in range(3):
            linha = []
            for j in range(3):
                btn = tk.Button(self.root, text="", width=8, height=4, font=("Arial", 16), command=lambda i=i, j=j: self.setButtonTextUser(i, j))
                btn.grid(row=i+1, column=j)  # +1 para não sobrescrever o label
                linha.append(btn)
            self.botoes.append(linha)

        tk.Label(self.root, text="Placar", font=("Arial", 15)).grid(row=5, column=0, columnspan=3)

        self.placarUser = tk.Label(self.root, text=f"Usuário: {self.pontosUser}", font=("Arial", 12))
        self.placarUser.place(x=10, y=435)
        
        self.placarComputer = tk.Label(self.root, text=f"Computador: {self.pontosComputer}", font=("Arial", 12))
        self.placarComputer.place(x=10, y=455)

        self.root.mainloop()

    def setButtonTextUser(self, i, j):
        if 0 <= i < 3 and 0 <= j < 3:
            self.botoes[i][j].config(text=self.tagUser, fg="blue")
        self.botoes[i][j].config(state=tk.DISABLED)
        self.root.update_idletasks()

        if not self.checkWinner():
            self.setButtonTextComputer()
    
    def setButtonTextComputer(self):
        time.sleep(1)
        availableButtons = []

        for i in range(3):
            for j in range(3):
                if self.botoes[i][j]['text'] == "":
                    availableButtons.append([i, j])


        if availableButtons:
            randomButton = random.choice(availableButtons)
            x, y = randomButton
            self.botoes[x][y].config(text=self.tagComputer, fg="red")
            self.botoes[x][y].config(state=tk.DISABLED)
        
        self.checkWinner()    
        
        return
        
    def checkWinner(self):
        vencedor = False
        botoesVencedores = []

        for linha in range(3):
            if self.botoes[linha][0]['text'] == \
               self.botoes[linha][1]['text'] == \
               self.botoes[linha][2]['text'] != '':
                vencedor = True

                botoesVencedores = [self.botoes[linha][0], self.botoes[linha][1], self.botoes[linha][2]]
                
                if self.botoes[linha][0]['text'] == self.tagUser:
                    self.pontosUser += 1
                else:
                    self.pontosComputer += 1
                
                break
          
        if not vencedor:
            for coluna in range(3):
                if self.botoes[0][coluna]['text'] == \
                   self.botoes[1][coluna]['text'] == \
                   self.botoes[2][coluna]['text'] != '':
                    vencedor = True
                    botoesVencedores = [self.botoes[0][coluna], self.botoes[1][coluna], self.botoes[2][coluna]]
                    if self.botoes[0][coluna]['text'] == self.tagUser:
                        self.pontosUser += 1
                    else:
                        self.pontosComputer += 1
                    break

        if not vencedor:
            # Diagonal principal
            if self.botoes[0][0]['text'] == self.botoes[1][1]['text'] == self.botoes[2][2]['text'] != '':
                vencedor = True
                botoesVencedores = [self.botoes[0][0], self.botoes[1][1], self.botoes[2][2]]
                if self.botoes[0][0]['text'] == self.tagUser:
                    self.pontosUser += 1
                else:
                    self.pontosComputer += 1
            # Diagonal secundária
            elif self.botoes[0][2]['text'] == self.botoes[1][1]['text'] == self.botoes[2][0]['text'] != '':
                vencedor = True
                botoesVencedores = [self.botoes[0][2], self.botoes[1][1], self.botoes[2][0]]
                if self.botoes[0][2]['text'] == self.tagUser:
                    self.pontosUser += 1
                else:
                    self.pontosComputer += 1

        if vencedor:
            for i in range(3):
                for botao in botoesVencedores:
                    botao.config(bg="green", fg="white")
                self.root.update()

                time.sleep(0.3)

                for botao in botoesVencedores:
                    botao.config(bg="SystemButtonFace", fg="black")
                self.root.update()
                time.sleep(0.3)

            self.placarUser.config(text=f"Usuário: {self.pontosUser}")
            self.placarComputer.config(text=f"Computador: {self.pontosComputer}")

            self.resetGame()
            
        # Verifica se todos os botões foram selecionados e não houve vencedor (deu velha)
        if not vencedor:
            todosPreenchidos = all(self.botoes[i][j]['text'] != '' for i in range(3) for j in range(3))
            if todosPreenchidos:
                vencedor = True
                for i in range(3):
                    for i in range(3):
                        for j in range(3):
                            self.botoes[i][j].config(bg="yellow")
                    
                    self.root.update()
                    time.sleep(0.3)
                    
                    for i in range(3):
                        for j in range(3):
                            self.botoes[i][j].config(bg="SystemButtonFace", fg="black")
                    self.root.update()
                    time.sleep(0.3)

                self.root.update()
                time.sleep(1)
                self.resetGame()
        return vencedor
    
    def resetGame(self):
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="", state=tk.NORMAL, bg="SystemButtonFace", fg="black")
        
        self.root.update_idletasks()

if __name__ == "__main__":
    main = Main()
    main.iniciarTela()