from flask import Flask, render_template, request
from graph.graph import Graph

app = Flask(__name__)


def create_graph(file):
    graph = Graph("Maze")
    lines = file.readlines()
    max_row = int(lines[0]) + 3
    max_col = int(lines[1]) - 1
    graph.rows = max_row - 3
    graph.cols = max_col + 1
    for row in range(4, len(lines)):
        line = lines[row]
        for col in range(0, max_col + 1):
            if line[col] == 48:
                graph.add_node(f'{row - 4},{col}')
                if col < max_col and line[col + 1] == 48:
                    graph.add_node(f'{row - 4},{col + 1}')
                    graph.add_arch(f'{row - 4},{col}', f'{row - 4},{col + 1}', 1)
                    graph.add_arch(f'{row - 4},{col + 1}', f'{row - 4},{col}', 1)
                if row < max_row and lines[row + 1][col] == 48:
                    graph.add_node(f'{row - 3},{col}')
                    graph.add_arch(f'{row - 4},{col}', f'{row - 3},{col}', 1)
                    graph.add_arch(f'{row - 3},{col}', f'{row - 4},{col}', 1)
    graph.add_start_end(lines[2][:-1].decode("utf-8"), lines[3][:-1].decode("utf-8"))
    return graph


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/maze', methods=['POST'])
def maze():
    file = request.files['file']
    graph = create_graph(file)
    rows = graph.rows
    cols = graph.cols
    start = graph.start.name
    end = graph.end.name
    nodes = list(graph.nodes.keys())
    path = graph.bfs()
    return render_template("maze.html", rows=rows, cols=cols, start=start, end=end, nodes=nodes, path=path)


if __name__ == '__main__':
    app.run()
