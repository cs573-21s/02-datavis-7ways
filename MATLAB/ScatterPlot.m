% Load the data
Data = readtable('../cars-sample.csv');

% convert manufacturer to a categorical data type
% https://www.mathworks.com/help/matlab/matlab_prog/convert-table-variables-containing-strings-to-categorical.html
numericManufacturer = categorical(Data.Manufacturer);

% Display it on a graph
% https://www.mathworks.com/help/matlab/ref/bubblechart.html
% Might be an r2020b thing
bubblechart(Data.Weight, Data.MPG, Data.Weight, numericManufacturer, 'MarkerFaceAlpha',0.50);
xlabel('Weight');
ylabel('MPG');
bubblesize([2,15]);
legend();
bubblelegend('Weight','Location','eastoutside');

% lots of cool things like zoom and pan included in MATLAB plots already!
