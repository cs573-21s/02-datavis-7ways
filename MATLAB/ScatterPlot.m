% Load the data
Data = readtable('../cars-sample.csv');

% convert manufacturer to colors
% matlab uses a silly 0 to 1 RGB scale instead of 0 to 255
newcolors = [];
for i=1:length(Data.Manufacturer)
    if string(Data.Manufacturer(i)) == 'bmw'
        newcolors = [newcolors; 31/255 119/255 180/255];
    elseif string(Data.Manufacturer(i)) == 'ford'
        newcolors = [newcolors; 255/255 127/255 14/255];
    elseif string(Data.Manufacturer(i)) == 'honda'
        newcolors = [newcolors; 44/255 160/255 44/255];
    elseif string(Data.Manufacturer(i)) == 'mercedes'
        newcolors = [newcolors; 214/255 39/255 40/255];
    else
        newcolors = [newcolors; 148/255 103/255 189/255];
    end
end

% Display it on a graph
% https://www.mathworks.com/help/matlab/ref/bubblechart.html
% Might be an r2020b thing
bubblechart(Data.Weight, Data.MPG, Data.Weight, newcolors, 'MarkerFaceAlpha',0.50);
xlabel('Weight');
ylabel('MPG');
bubblesize([2,15]);
legend();
bubblelegend('Weight','Location','eastoutside');

% lots of cool things like zoom and pan included in MATLAB plots already!
