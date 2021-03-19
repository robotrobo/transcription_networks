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
    }
  }

  options.nodes = {
    color: "red",

  };

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

    }
  });
}