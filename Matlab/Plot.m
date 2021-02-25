T = readtable('cars-sample.csv');

x = T{:,8};
y = T{:,4};
c = T{:,3};

color = [
    183/255 183/255 74/255;
    125/255 203/255 243/255;
    243/255 172/255 172/255;
    128/255 213/255 176/255;
    136/255 205/255 241/255;
]; 


gscatter(x,y,c,color,'.', x/100)

set(gca,'Color',[236/255, 236/255, 236/255])

xlabel('Weight');
ylabel('MPG');
xlim([1500, 5000]);
ylim([5, 47]);
