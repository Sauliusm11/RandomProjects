import pandas as pd

def find_best_team_assignment(roles):
    current = [0,0,0,0,0]
    best = [0,0,0,0,0]
    sum = 0
    best_sum = 0
    for i in range(0,12):
        if roles[0][i] > 0:
            current[0] = roles[0][i]
            for j in  range(0,12):
                if roles[1][j] > 0 and j != i:
                    current[1] = roles[1][j]
                    for k in range(0,12):
                        if roles[2][k] > 0 and k != i and k != j:
                            current[2] = roles[2][k]
                            for l in range(0,12):
                                if roles[3][l] > 0 and l != i and l != j and l != k:
                                    current[3] = roles[3][l]
                                    for h in range(0,12):
                                        if roles[4][h] > 0 and h != i and h != j and h != k and h != l:
                                            current[4] = roles[4][h]
                                            sum = 0
                                            for s in range(0,5):
                                                sum+= current[s]
                                            if best_sum< sum:
                                                best = current.copy()
                                                best_sum = sum
    return best, best_sum
                            
# Read data from Excel file
excel_file_path = './Values.xlsx'
df = pd.read_excel(excel_file_path)
print(df)
df.columns.name = None
df = df.transpose()
df = df.values.tolist()
# print(df)
roles = df
best_assignment, best_score = find_best_team_assignment(roles)

print("Best Team Assignment:", best_assignment)
print("Best Team Score:", best_score)
