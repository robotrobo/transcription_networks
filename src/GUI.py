from flask import Flask, render_template, request, redirect
from graph.graph import generate_graph
import uuid

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
