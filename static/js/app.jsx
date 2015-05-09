var Map = React.createClass({
	componentDidMount: function() {
		var node = React.findDOMNode(this);
		console.log(node);
		// create a map in the "map" div, set the view to a given place and zoom
		var map = L.map(node).setView([50.1072, 8.6626], 13);

		// add an OpenStreetMap tile layer
		L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
		}).addTo(map);
		
		$.getJSON('/geodata/', function(data) {
			L.geoJson(data, {
			    style: function (feature) {
			        return {color: "#ff0000"};
			    },
			    onEachFeature: function (feature, layer) {
			        layer.bindPopup(feature.properties.description);
			    }
			}).addTo(map);
		});
		
		
	},
	render: function() {
		return(
			<div className="mymap">
			</div>
		);
	}
})

var DBHackApp = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        <h1>Hello, world!</h1>
				<Map />
      </div>
    );
  }
});

React.render(
  <DBHackApp />,
  document.getElementById('app')
);
