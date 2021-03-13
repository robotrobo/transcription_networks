function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    var text = ""
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
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

  DOTstring =  readTextFile(dot_file_name);
  console.log(DOTstring);

  const container = document.getElementById('mynetwork');

  var parsedData = vis.parseDOTNetwork(DOTstring);

  var data = {
    nodes: parsedData.nodes,
    edges: parsedData.edges
  };

  var options = parsedData.options;

  // you can extend the options like a normal JSON variable:
  options.nodes = {
    color: "red"
  };

  // initialize your network!
  network = new vis.Network(container, data, options);
}

function addConnections(elem, index) {
  elem.connections = network.getConnectedNodes(index);
}



function exportNetwork() {

  var nodes = objectToArray(network.getPositions());

  nodes.forEach(addConnections);

  // pretty print node data
  var exportValue = JSON.stringify(nodes, undefined, 2);

  console.log(exportValue);
}


function objectToArray(obj) {
  return Object.keys(obj).map(function (key) {
    obj[key].id = key;
    return obj[key];
  });
}
