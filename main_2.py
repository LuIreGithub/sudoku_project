from simple_solver import  SimpleSolver


def read_sudoku(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()  
            row = []
            for char in line:
                if char == "_":  
                    row.append(0)
                else:
                    row.append(int(char))
            grid.append(row)
    return grid

sudoku = read_sudoku("/Users/luciaireneespitia/Downloads/evilsudoku.txt")

for row in sudoku:
    print(row)


def print_grid(original, solved):
    for i in range(9):
        row_display = []
        for j in range(9):
            if original[i][j] == 0:
                row_display.append(f"[{solved[i][j]}]")  
            else:
                row_display.append(str(solved[i][j]))      
        print(" ".join(row_display))

original_grid = read_sudoku("/Users/luciaireneespitia/Downloads/sudoku.txt")

print("\n" + "="*30 + "\n")

solver = SimpleSolver([row[:] for row in original_grid])  

solver.solve()
print_grid(original_grid, solver.grille)