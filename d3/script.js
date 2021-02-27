// import * as d3 from 'd3';

console.log(d3); // test if d3 is loaded

let width = 600;
let height = 500;
let margin = {
  top: 20, 
  right: 20, 
  bottom: 30, 
  left: 30
}

const COLORS = {
  "bmw": "red",
  "ford": "yellowgreen",
  "honda": "bluegreen",
  "mercedes": "blue",
  "toyota": "pink"
};

let svg = d3.select('#car-chart')
  .attr('width', width)
  .attr('height', height);

const LOAD_DATA = new Promise((resolve, reject) => {
  Promise.all([
    d3.csv("../cars-sample.csv"),
  ]).then(values => {
    console.log('All data loaded!');
    debugger;
    buildVis(values[0])
    resolve(values);
  }).catch(err => {
    console.error(`Error loading the csv data: ${err}`);
    reject(err);
  })
  debugger;
});

function buildVis(dataArray){
  // Set a common scale and axes using the first dataset
  let x = d3.scaleLinear()
    .domain([1500, 5010])
    .range([margin.left, width - margin.right])

  let y = d3.scaleLinear()
    .domain([9, 46])
    .range([height - margin.bottom, margin.top])

  xAxis = g => g
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(width / 80).tickSizeOuter(0))

  yAxis = g => g
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y))
    .call(g => g.select(".domain").remove())
    .call(g => g.select(".tick:last-of-type text").clone()
        .attr("x", 3)
        .attr("text-anchor", "start")
        .attr("font-weight", "bold")
        .text(dataArray.MPG))

  svg.append("g")
    .selectAll("dot")
    .data(dataArray)
    .enter()
    .append("circle")
      .attr("cx", d => x(d.Weight))
      .attr("cy", d => y(d.MPG))
      .attr("r", d => 0.002 * d.Weight)
      .attr("opacity", 0.5)
      .attr("fill", d => COLORS[d.Manufacturer])
      .attr("make-name", d => d.Manufacturer)
      .attr("model-name", d => d.Car)


  svg.append("g")
    .call(xAxis);

  svg.append("g")
    .call(yAxis);

}
