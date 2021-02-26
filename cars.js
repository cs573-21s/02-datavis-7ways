d3 = require("d3@6")

height = 600
margin = 25

// data = Object.assign(d3.csvParse(await FileAttachment("cars_cleaned.csv").text(), ({Car, Weight: x, MPG: y}) => ({Car, x: +x, y: +y})), {x: "Miles per gallon →", y: "↑ Horsepower"})

// var x = d3.scaleLinear()
//     .domain([1500, 5250]).nice()
//     // .range([0, width ])
//     .range([margin, width - margin])

// var y = d3.scaleLinear()
//     .domain([5, 50]).nice()
//     .range([height - margin, margin])

// var xAxis = g => g
//     .attr("transform", `translate(0,${height - margin})`)
//     .call(d3.axisBottom(x))
//     .call(g => g.select(".domain").remove())
//     .call(g => g.append("text")
//         .attr("x", width)
//         .attr("y", margin - 4)
//         .attr("fill", "currentColor")
//         .attr("text-anchor", "end")
//         .text(data.x))

// var yAxis = g => g
//     .attr("transform", `translate(${margin},0)`)
//     .call(d3.axisLeft(y))
//     .call(g => g.select(".domain").remove())
//     .call(g => g.append("text")
//         .attr("x", -margin)
//         .attr("y", 10)
//         .attr("fill", "currentColor")
//         .attr("text-anchor", "start")
//         .text(data.y))

// var grid = g => g
//     .attr("stroke", "currentColor")
//     .attr("stroke-opacity", 0.1)
//     .call(g => g.append("g")
//     .selectAll("line")
//     .data(x.ticks())
//     .join("line")
//         .attr("x1", d => 0.5 + x(d))
//         .attr("x2", d => 0.5 + x(d))
//         .attr("y1", margin.top)
//         .attr("y2", height - margin.bottom))
//     .call(g => g.append("g")
//     .selectAll("line")
//     .data(y.ticks())
//     .join("line")
//         .attr("y1", d => 0.5 + y(d))
//         .attr("y2", d => 0.5 + y(d))
//         .attr("x1", margin.left)
//         .attr("x2", width - margin.right));



// function make_chart() {
//     const svg = d3.create("svg")
//         .attr("viewBox", [0, 0, width, height])
  
//     svg.append("g")
//         .call(xAxis)
  
//     svg.append("g")
//         .call(yAxis)
  
//     svg.append("g")
//         .call(grid);
  
//     svg.append("g")
//         .attr("stroke", "steelblue")
//         .attr("stroke-width", 1.5)
//         .attr("fill", "none")
//       .selectAll("circle")
//       .data(data)
//       .join("circle")
//         .attr("cx", d => x(d.x))
//         .attr("cy", d => y(d.y))
//         .attr("r", 3);
  
//     svg.append("g")
//         .attr("font-family", "sans-serif")
//         .attr("font-size", 10)
//       .selectAll("text")
//       .data(data)
//       .join("text")
//         .attr("dy", "0.35em")
//         .attr("x", d => x(d.x) + 7)
//         .attr("y", d => y(d.y))
//         .text(d => d.name);
  
//     return svg.node();
//   }


// set the dimensions and margins of the graph
var margin = {top: 10, right: 20, bottom: 30, left: 50},
    width = 500 - margin.left - margin.right,
    height = 420 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/4_ThreeNum.csv", function(data) {

  // Add X axis
  var x = d3.scaleLinear()
    .domain([0, 10000])
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([35, 90])
    .range([ height, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));

  // Add a scale for bubble size
  var z = d3.scaleLinear()
    .domain([200000, 1310000000])
    .range([ 1, 40]);

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
      .attr("cx", function (d) { return x(d.gdpPercap); } )
      .attr("cy", function (d) { return y(d.lifeExp); } )
      .attr("r", function (d) { return z(d.pop); } )
      .style("fill", "#69b3a2")
      .style("opacity", "0.7")
      .attr("stroke", "black")
      
})