let data, scales, svg, colors = {};

let colorList = ["pink", "purple", "green", "yellow", "blue", "red"];

function initializeData() {
    var request = new XMLHttpRequest();
    request.open("GET", "../cars-sample.csv");
    request.onreadystatechange = () => {
        if(request.readyState === 4 && (request.status === 200 || request.status === 0)) {
            csvToObject(request.responseText);
            svg = d3.select("#draw");
            resize();
        }   
    }
    request.send();
}

function csvToObject(csv) {
    if(typeof csv == 'undefined' || typeof csv == 'null')
        throw new Error("There is no data to turn into an object.");
    data = [];
    let rows = csv.replaceAll("\"", "").split('\n'),
        headers = rows[0].split(',');
    for(var i = 0; i < headers.length; i++)
        if(headers[i].length === 0) headers[i] = "null";
    for(var i = 1; i < rows.length; i++) {
        let obj = {}, row = rows[i].split(','), add = true;
        for(var j = 0; j < row.length; j++) {
            if(row[j] == "NA" || row[j] == "") {
                add = false;
                break;
            }
            obj[headers[j]] = row[j];
        }  
        if(add) data.push(obj);
    }
}

function getOrCreateColor(val) {
    if(typeof colors[val] == "undefined" || typeof colors[val] == "null")
        colors[val] = colorList.pop();
    return colors[val];
}

function updateScales() {
    let draw = document.getElementById("draw"),
        scale = (draw.clientWidth > draw.clientHeight ? draw.clientHeight : draw.clientWidth) - 100;
    scales = {
        def: scale,
        weight: d3.scaleLinear().domain([1000, 5000]).range([0, scale]),
        mpg: d3.scaleLinear().domain([5, 50]).range([scale, 0])
    }
    svg.append("g")
        .attr("transform", "translate(100, " + (scale + 10) + ")")
        .call(d3.axisBottom().scale(scales.weight));
    svg.append("g")
        .attr("transform", "translate(100, 10)")
        .call(d3.axisLeft().scale(scales.mpg));
    svg.append("text")
        .attr("text-anchor", "end")
        .attr("x", scale / 2 + 100)
        .attr("y", scale + 50)
        .text("Weight");
    svg.append("text")
        .attr("text-anchor", "end")
        .attr("transform", "rotate(-90)")
        .attr("y", 50)
        .attr("x", - scale / 2)
        .text("MPG")
}

function resize() {
    svg.selectAll("*").remove();
    updateScales();
    svg.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", c => scales.weight(c.Weight) + 100)
        .attr("cy", c => scales.mpg(c.MPG) + 10)
        .attr("r", c => c.Weight / 600.0)
        .attr("stroke", _ => "#000000")
        .attr("fill", c => getOrCreateColor(c.Manufacturer))
        .attr("opacity", _ => "50%");

}

window.onload = initializeData;
window.addEventListener("resize", resize);