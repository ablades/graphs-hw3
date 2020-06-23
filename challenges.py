from graph import Graph, Vertex


# problem 1
def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    graph = Graph(is_directed=False)

    #one possible approach
        #build a graph

            #loop over all verticies 
                #check if a vertex has been visited
                # if it has not perform a bfs and increment land count
                # if it has already been seen its already connected - skip

            # return count == # of islands

    # second approach
        # just call connected componenets :))

    pass