function readTextFile(file) {
  var rawFile = new XMLHttpRequest();
  var text = ""
  rawFile.open("GET", file, false);
  rawFile.onreadystatechange = function () {
    if (rawFile.readyState === 4) {
      if (rawFile.status === 200 || rawFile.status == 0) {
        var allText = rawFile.responseText;
        // alert(allText)
        // return allText;
        text = allText;
      }
    }
  }
  rawFile.send(null);
  return text;
}

var network;
var deleteEdge = false;

function edit_node(dot_file_name){

  var old_id = document.getElementById("edit_seq").getAttribute('node-id');
  var id = document.getElementById("new_id").value;
  var seq = document.getElementById("new_seq").value;
  var len = document.getElementById("new_len").value;


  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/edit_node");
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(`name=${dot_file_name}&&old_id=${old_id}&&id=${id}&&seq=${seq}&&len=${len}`);
  xhttp.addEventListener('loadend', (_) => location.reload());


}




function refresh_colors(file_name){
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/refresh_graph");
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(`name=${file_name}`);
  xhttp.addEventListener('loadend', (_) => location.reload());
}

function save_graph(file_name){
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "/save_graph");
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  new_name = prompt("Enter the new file name");
  if(new_name == null) return ;
  xhttp.send(`old_name=${file_name}&&new_name=${new_name}`);
  xhttp.addEventListener('loadend', (_) => window.location = `/view_graph/?name=/static/generated_graphs/${new_name}`);

}

function createGraph(dot_file_name) {

  DOTstring = readTextFile(dot_file_name);
  console.log(DOTstring);

  const container = document.getElementById('mynetwork');

  var parsedData = vis.parseDOTNetwork(DOTstring);

  var data = {
    nodes: parsedData.nodes,
    edges: parsedData.edges
  };

  // var options = parsedData.options;
  options = {
    interaction: {
      hover: true
    },
    manipulation: {
      enabled: true,
    },
    edges: {
      color: 'gray'
    }


  }
  // options = {
  // }
  // initialize your network!
  network = new vis.Network(container, data, options);
  network.on("controlNodeDragEnd", function (params) {
    params.event = "[original event]";
    if (params.controlEdge.from != undefined && params.controlEdge.to != undefined) {
      console.log("controlNodeDragEnd Event:", params.controlEdge);
      // Ask flask to modify our dot file
      var xhttp = new XMLHttpRequest();
      xhttp.open("POST", "/add_edge");
      xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xhttp.send(`from=${params.controlEdge.from}&to=${params.controlEdge.to}&name=${dot_file_name}`);
      xhttp.addEventListener('loadend', (_) => location.reload());
    }
  });

  network.on("click", function (params) {

    let edit_div = document.getElementById("edit_seq");
    if (params.nodes.length != 0) {
      let node_options = network.body.nodes[params.nodes[0]].options;
      let show_div = document.getElementById("show_seq");
      edit_div.removeAttribute('hidden'); 
      edit_div.setAttribute('node-id', node_options.id); 


      show_div.innerHTML =
      `id  : ${node_options.id} <br>
       seq : ${node_options.seq} <br>
       len : ${node_options.len}
      `
      console.log(params)
    }
    else {
      edit_div.setAttribute('hidden', 'true'); 
      edit_div.removeAttribute('node-id');
    }



    var delete_button = document.getElementsByClassName("vis-delete")[0];

    console.log(delete_button);

    if (delete_button != undefined) {
      let edge;
      // let node;


      if (params.edges.length != 0) {
        edge = network.body.edges[params.edges[0]];
      }

      delete_button.onpointerdown = function () {

        console.log("Deleting edge :\n");
        // console.log(edge);
        // Ask flask to remove the edge from the dot file
        var xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/remove_edge");
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send(`from=${edge.fromId}&to=${edge.toId}&name=${dot_file_name}`);
        xhttp.addEventListener('loadend', (_) => location.reload());
      };
    }
  });
}