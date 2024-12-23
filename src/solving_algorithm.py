import solver

def add_steps(steps, letter):
    if steps == "1":
        return letter + '+'
    if steps == "2":
        return letter + '+' + letter + '+'
    return letter + '-'

def output_for_steppers(output_str):
    new_str = ""
    for i in range(len(output_str)):
        if i % 3 == 0:
            letter = output_str[i]
        if i % 3 == 1:
            steps = output_str[i]
            new_str += add_steps(steps, letter)
        if output_str[i] == "(":
            break
    return new_str  

def solve_cube(scrambled_cube):
    solving_moves = solver.solve(scrambled_cube)
    return output_for_steppers(solving_moves)
