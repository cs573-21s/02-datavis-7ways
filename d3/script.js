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

COLORS = {
  'bmw': '#E360EB88',
  'ford': '#EBCD6C88',
  'honda': '#9155EB88',
  'mercedes': '#86EB3D88',
  'toyota': '#495FEB88'
}

let svg = d3.select('#car-chart')
  .attr('width', width)
  .attr('height', height);

const LOAD_DATA = new Promise((resolve, reject) => {
  Promise.all([
    d3.csv("../cars-sample.csv"),
  ]).then(values => {
    console.log('All data loaded!');
    buildVis(values[0])
    resolve(values);
  }).catch(err => {
    console.error(`Error loading the csv data: ${err}`);
    reject(err);
  })
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

  // // Add the text label for the x axis
  // svg.append("text")
  // .attr("transform", "translate(" + (width / 2) + " ," + (height + margin.bottom) + ")")
  // .style("text-anchor", "middle")
  // .text("Weight");

  svg.append("g")
    .call(yAxis);

  // // Add the text label for the Y axis
  // svg.append("text")
  //   .attr("transform", "rotate(-90)")
  //   .attr("y", 0 - margin.left)
  //   .attr("x",0 - (height / 2))
  //   .attr("dy", "1em")
  //   .style("text-anchor", "middle")
  //   .text("MPG");

  svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "end")
    .attr("x", width)
    .attr("y", height - 6)
    .text("Weight");

  svg.append("text")
    .attr("class", "y label")
    .attr("text-anchor", "end")
    .attr("y", 6)
    .attr("dy", ".75em")
    .attr("transform", "rotate(-90)")
    .text("MPG");

}
