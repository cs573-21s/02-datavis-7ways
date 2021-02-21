let data;

function initializeData() {
    var request = new XMLHttpRequest();
    request.open("GET", "../cars-sample.csv");
    request.onreadystatechange = () => {
        if(this.readyState === 4 && (this.status === 200 || this.status === 0)) {
            csvToObject(this.responseText);
        }   
    }
    request.send();
}

function csvToObject(csv) {
    if(typeof csv == 'undefined' || typeof csv == 'null')
        throw new Error("There is no data to turn into an object.");
    data = [];
    let rows = csv.replaceAll("\"", "").split('\n');
    headers = rows[0].split(',');
    var i;
    for(i = 0; i < headers.length; i++)
        if(headers[i].length === 0) headers[i] = "null";
    for(i = 1; i < rows.length; i++) {
        let obj = {}, row = rows[i].split(',');
        console.log(row);
        for(i = 0; i < row.length; i++)
            obj[headers[i]] = row[i];
        data.push(obj);
    }
    console.log(data);
}

window.onload = initializeData;