X = [[12, 7],
     [4, 5],
     [3, 8],[1,2]]

result = [[0, 0, 0,0],
          [0, 0, 0,0]]

# Duyệt qua các hàng
for i in range(len(X)):
    # Duyệt qua các cột
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)
