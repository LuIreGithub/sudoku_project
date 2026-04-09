# Deuxième strategie
class SimpleSolver:
    def __init__(self, grille):
        self.grille = grille

    def solve(self):
        changed = True
        while changed:
            changed = False
            for i in range(9):
                for j in range(9):
                    if self.grille[i][j] == 0:
                        possibilities = [n for n in range(1, 10) if self.is_valid(n, i, j)]
                        if len(possibilities) == 1:
                            self.grille[i][j] = possibilities[0]
                            changed = True
        return all(all(cell != 0 for cell in row) for row in self.grille)

    def is_valid(self, num, row, col):
        
        if num in self.grille[row]:
            return False
        
        for i in range(9):
            if self.grille[i][col] == num:
                return False
        
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y*3, box_y*3+3):
            for j in range(box_x*3, box_x*3+3):
                if self.grille[i][j] == num:
                    return False
        return True

    