import random


class IBot():
    def __init__(self, tagComputer):
        self.estrategia = None
        self.availablePositions = None
        self.tagComputer = tagComputer
        self.corners = [[0,0], [0,2], [2,0], [2,2]]
        self.buttons = None
        self.computerCorners = []
        pass
        

    def decidirEstrategia(self, availablePositions, buttons):
        self.availablePositions = availablePositions
        self.buttons = buttons

        if not self.estrategia:
            varEstrategias = []
            if sum(1 for i in self.corners if i in availablePositions) >= 3:
                varEstrategias.append("corner")
            if len(availablePositions) == 9:
                varEstrategias.append("center")
            if len(availablePositions) == 8:
                varEstrategias.append("block")

            if len(availablePositions) > 0:
                self.estrategia = random.choice(varEstrategias) if varEstrategias else "random"
        
        print(self.estrategia)

        match self.estrategia:
            case "corner":
                return self.estrategiaCorners()
            case "center":
                return self.estrategiaCenter()
            case "block":
                return self.estrategiaBlock()
            case "random":
                return self.estrategiaRandom()

    
    def estrategiaCorners(self):
        if len(self.computerCorners) < 3:
            for corner in self.corners:
                if corner in self.availablePositions:
                    self.computerCorners.append(corner)
                    return corner
        else:
            if self.computerCorners == [[0,0], [0,2], [2,0]]:
                recommended_moves = [[0,1], [1,0], [1,1]]
                for move in recommended_moves:
                    if move in self.availablePositions:
                        return move
            elif self.computerCorners == [[0,0], [0,2], [2,2]]:
                recommended_moves = [[0,1], [1,1], [1,2]]
                for move in recommended_moves:
                    if move in self.availablePositions:
                        return move
            elif self.computerCorners == [[0,0], [2,0], [2,2]]:
                recommended_moves = [[2,1], [1,1], [1,0]]
                for move in recommended_moves:
                    if move in self.availablePositions:
                        return move
            elif self.computerCorners == [[0,2], [2,0], [2,2]]:
                recommended_moves = [[1,1], [1,2], [2,1]]
                for move in recommended_moves:
                    if move in self.availablePositions:
                        return move
            return random.choice(self.availablePositions)

    def estrategiaCenter(self):
        if [1, 1] in self.availablePositions:
            return [1, 1]
        elif [1, 1] not in self.availablePositions and self.buttons[1][1]['text'] == self.tagComputer:
            for pos in self.availablePositions:
                # Check if the button is empty
                if self.buttons[pos[0]][pos[1]]['text'] == '':
                    # Find the opposite position
                    opposite = [2 - pos[0], 2 - pos[1]]
                    # If the opposite position is filled by the user (not computer and not empty), skip
                    if self.buttons[opposite[0]][opposite[1]]['text'] != '' and self.buttons[opposite[0]][opposite[1]]['text'] != self.tagComputer:
                        continue
                    return pos
            return random.choice(self.availablePositions)
            
    def estrategiaBlock(self):
        # Verifica linhas
        for i in range(3):
            user_positions = [j for j in range(3) if self.buttons[i][j]['text'] != '' and self.buttons[i][j]['text'] != self.tagComputer]
            empty_positions = [j for j in range(3) if self.buttons[i][j]['text'] == '']
            if len(user_positions) == 2 and len(empty_positions) == 1:
                return [i, empty_positions[0]]

        # Verifica colunas
        for j in range(3):
            user_positions = [i for i in range(3) if self.buttons[i][j]['text'] != '' and self.buttons[i][j]['text'] != self.tagComputer]
            empty_positions = [i for i in range(3) if self.buttons[i][j]['text'] == '']
            if len(user_positions) == 2 and len(empty_positions) == 1:
                return [empty_positions[0], j]

        # Verifica diagonal principal
        user_positions = [i for i in range(3) if self.buttons[i][i]['text'] != '' and self.buttons[i][i]['text'] != self.tagComputer]
        empty_positions = [i for i in range(3) if self.buttons[i][i]['text'] == '']
        if len(user_positions) == 2 and len(empty_positions) == 1:
            return [empty_positions[0], empty_positions[0]]

        # Verifica diagonal secundária
        user_positions = [i for i in range(3) if self.buttons[i][2-i]['text'] != '' and self.buttons[i][2-i]['text'] != self.tagComputer]
        empty_positions = [i for i in range(3) if self.buttons[i][2-i]['text'] == '']
        if len(user_positions) == 2 and len(empty_positions) == 1:
            return [empty_positions[0], 2-empty_positions[0]]

        # Se não houver ameaça, escolha aleatoriamente
        return random.choice(self.availablePositions)
    
    def estrategiaRandom(self):
        return random.choice(self.availablePositions)

