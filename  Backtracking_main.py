import os
import copy
from Backtracking import BacktrackingSolver


def lire_sudoku(nom_fichier):
   
  
    if not os.path.isabs(nom_fichier):
        script_dir = os.path.dirname(__file__)
        nom_fichier = os.path.join(script_dir, nom_fichier)

    grid = []
    with open(nom_fichier, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:  
                continue
            row = [int(ch) if ch.isdigit() else 0 for ch in line]
            grid.append(row)
    return grid




def print_grid(original, solved):
    for i in range(9):
        row_display = []
        for j in range(9):
            if original[i][j] == 0:
                row_display.append(f"[{solved[i][j]}]") 
            else:
                row_display.append(str(solved[i][j]))     
        print(" ".join(row_display))
       

if __name__ == "__main__":
    nom_fichier = "sudoku.txt"  # Ecrivez ici le nom du fichier
    original_grid = lire_sudoku(nom_fichier)

    
    grid_to_solve = copy.deepcopy(original_grid)

    
    print("Sudoku Original:")
    print_grid(original_grid, original_grid)

    print("="*40 + "\n")

    
    solver = BacktrackingSolver(grid_to_solve)
    solver.solve()  
    solution = solver.grille

    print("Solution Backtracking:")
    print_grid(original_grid, solution)