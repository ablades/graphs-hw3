from graph import Graph, Vertex


# problem 1
def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return
    the number of islands.
    """

    graph = Graph(is_directed=False)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # position of the item as well as id
            pos = len(grid[i]) * i + j

            if grid[i][j] == 1:
                # add vertex to graph
                graph.add_vertex(pos)

                # look up bounds and check connection
                if i > 0 and grid[i - 1][j] == 1:
                    adjPos = len(grid[i - 1]) * (i - 1) + j
                    graph.add_edge(pos, adjPos)

                # look left bounds and check connection
                if j > 0 and grid[i][j - 1] == 1:
                    adjPos = len(grid[i]) * i + (j - 1)
                    graph.add_edge(pos, adjPos)

    return len(graph.find_connected_components())


if __name__ == "__main__":

    # Test Cases
    map1 = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    print(numIslands(map1))

    map2 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    print(numIslands(map2))
