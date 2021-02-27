// let Chart = require('chart.js');
// let d3 = require('d3');

ctx = document.getElementById('car-chart');
LOAD_DATA = d3.csv("../cars-sample.csv");
BRANDS = ['bmw', 'ford', 'honda', 'mercedes', 'toyota'];
COLORS = {
    'bmw': '#E360EB88',
    'ford': '#EBCD6C88',
    'honda': '#9155EB88',
    'mercedes': '#86EB3D88',
    'toyota': '#495FEB88'
}

LOAD_DATA.then(data => {
    console.log('data loaded');
    let datasets = [];
    for(let brand of BRANDS) {
        let transformed_data = [];
        for (let row of data) {
            if (!isNaN(parseFloat(row['MPG'])) && row['Manufacturer'] === brand){
                transformed_data.push({
                    x: parseFloat(row['Weight']),
                    y: parseFloat(row['MPG']),
                    r: 0.005 * parseFloat(row['Weight'])
                });
            }
        }
        datasets.push({
            label: [brand],
            data: transformed_data,
            backgroundColor: COLORS[brand]
        });
        
    }

    let chart = new Chart(ctx, {
        type: 'bubble',
        data: {
            datasets: datasets
        },
        options: {
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'MPG'
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Weight'
                    }
                }]
            },
            title: {
                display: true,
                fontSize: "24",
                text: 'Weight vs MPG ChartJS'
            }
        }
    });

});