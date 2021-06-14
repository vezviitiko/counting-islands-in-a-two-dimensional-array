class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # Функция для проверки, если данная ячейка
    # (строка, столбец) может быть включен в DFS
    def isSafe(self, i, j, visited):

        # номер строки находится в диапазоне, номер столбца
        # находится в диапазоне и значение 1
        # и еще не посещал
        return (i >= 0 and i < self.ROW and 
                j >= 0 and j < self.COL and 
                not visited[i][j] and self.graph[i][j])


    # Полезная функция для создания DFS для 2D
    # булева матрица. Это только считает
    # 8 соседей как смежные вершины
    def DFS(self, i, j, visited):

        # Эти массивы используются для получения строки и
        # номера столбцов 8 соседей
        # данной ячейки
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];

        # Отметить эту ячейку как посещенную
        visited[i][j] = True

        # Повторить для всех подключенных соседей
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    # Основная функция, которая возвращает
    # количество островов в данном логическом значении
    # 2D матрица

    def countIslands(self):
        # Создайте массив bool для отметки посещенных ячеек.
        # Первоначально все ячейки не посещены
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

        # Инициализировать считать как 0 и путешествовать
        # через все клетки
        # заданная матрица

        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # Если ячейка со значением 1 еще не посещена,
                # тогда новый остров найден
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # Посетите все клетки на этом острове
                    # и увеличение числа островов
                    self.DFS(i, j, visited)
                    count += 1
        return count

graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])
g = Graph(row, col, graph)
print("Number of islands is:", g.countIslands())
