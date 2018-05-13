dist = []

def floyd(input):
    for k in range(0,len(input)):
        for i in range(0,len(input)):
            for j in range(0,len(input)):
                if dist[i,j] > dist[i][k] + dist[k][j]:
                    dist[i, j] = dist[i][k] + dist[k][j]