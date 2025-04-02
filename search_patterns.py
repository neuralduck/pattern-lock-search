import matplotlib.pyplot as plt
graph = {
    1: (2, 4, 5, 6, 8),
    2: (1, 3, 4, 5, 6, 7, 9),
    3: (2, 4, 5, 6, 8),
    4: (1, 2, 3, 5, 7, 8, 9),
    5: (1, 2, 3, 4, 6, 7, 8, 9),
    6: (1, 2, 3, 5, 7, 8, 9),
    7: (2, 4, 5, 6, 8),
    8: (1, 3, 4, 5, 6, 7, 9),
    9: (2, 4, 5, 6, 8)
}

def search(graph: dict[int, tuple], length = 4):
    patterns = set()
    def dfs(pattern: list):
        if len(pattern) == length:
            patterns.add(tuple(pattern))
            return
        start = pattern[-1]
        for node in graph[start]:
            if node not in pattern:
                dfs(pattern + [node])

    for node in graph.keys():
        dfs([node])
    
    return patterns



if __name__ == "__main__":
    length = int(input("length of the pattern to search (pick a num between 4 to 9): "))
    assert (length >=4) and (length <=9)
    result = sorted(search(graph, length), key=lambda x: int(''.join(map(str, x))))
    print(f"{len(result)} patterns found of length {length}")
    gen_image = input("want to generate the images? (y/n)")
    assert gen_image in ('y', 'n')
    if gen_image == 'y':
        for i, sample in enumerate(result):
            nodes = {
                1: (0, 2), 2: (1, 2), 3: (2, 2),
                4: (0, 1), 5: (1, 1), 6: (2, 1),
                7: (0, 0), 8: (1, 0), 9: (2, 0),
            }

            edges = list(zip(sample, sample[1:])) 

            plt.figure(figsize=(3, 3))


            for n1, n2 in edges:
                x_vals, y_vals = [nodes[n1][0], nodes[n2][0]], [nodes[n1][1], nodes[n2][1]]
                plt.plot(x_vals, y_vals, 'k-', lw=2)

            for x, y in nodes.values():
                plt.plot(x, y, 'ro', markersize=8)

            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.axis("off")

            plt.savefig(f"pattern_{i+1}.jpg", dpi=300, bbox_inches="tight")
            print(i+1, "generated")
    else:
        print("bye")
