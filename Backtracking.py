#Backtracking strategie
class BacktrackingSolver:
    def __init__(self, grille):
        self.grille = grille

    def solve(self):
        vide = self.find_empty()
        if not vide:
            return True
        row, col = vide
        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.grille[row][col] = num
                if self.solve():
                    return True
                self.grille[row][col] = 0
        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grille[i][j] == 0:
                    return (i, j)
        return None

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


