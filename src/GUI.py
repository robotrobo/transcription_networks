from flask import Flask, render_template, request, redirect
from graph.graph import generate_graph, insert_edge, delete_edge, refresh_colors, edit_node
import uuid
import pathlib
import shutil
GRAPH_DIR = "static/generated_graphs"


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/gen_graph', methods=['POST'])
def gen_graph():
    form = request.form
    data = [form["nodes"], form["edges"]]
    dot_string = ''
    graph_name = f"{GRAPH_DIR}/{uuid.uuid1()}.dot"
    try:
        generate_graph(data, graph_name)
    except ValueError:
        return "Please enter integers in the fields"
    

    return redirect(f"/view_graph?name=/{graph_name}")

@app.route('/view_graph/')
def view_graph():
    return render_template('view_graph.html', value=request.args.get('name'))

@app.route('/add_edge', methods=['POST'])
def add_edge():
    form = request.form
    data = [form["from"], form["to"]]
    insert_edge(form["name"], form["from"], form["to"])
    print(data)
    print(form["name"])
    return "Okay"

@app.route('/remove_edge', methods=['POST'])
def remove_edge():
    form = request.form
    data = [form["from"], form["to"]]
    delete_edge(form["name"], form["from"], form["to"])
    print(data)
    print(form["name"])
    return "Okay"

@app.route('/list_graphs', methods=['GET'])
def list_graphs():
    graph_names = [g.name for g in pathlib.Path(GRAPH_DIR).glob('*')]
    return render_template("list_graphs.html", graphs=graph_names, dir=GRAPH_DIR)

@app.route('/refresh_graph', methods=['POST'])
def refresh_graph():
    form = request.form
    refresh_colors(form["name"])
    return "Okay"

@app.route('/save_graph', methods=['POST'])
def save_graph():
    form = request.form
    # Ignore the leading slash in the old_name
    shutil.copyfile(form["old_name"][1:], f"{GRAPH_DIR}/{form['new_name']}")
    return "Okay"

@app.route('/edit_node', methods=['POST'])
def edit_node_graph():
    form = request.form
    edit_node(form["name"], form["old_id"],form["id"],form["seq"],form["len"])
    return "Okay"