data = readmatrix('cars.csv');

x1 = data(:, 5);
y1 = data(:, 6);

x2 = data(:, 9);
y2 = data(:, 10);

x3 = data(:, 13);
y3 = data(:, 14);

x4 = data(:, 17);
y4 = data(:, 18);

x5 = data(:, 21);
y5 = data(:, 22);

hold all
bubblechart(x1,y1, x1/25, "#b5b639",'MarkerFaceAlpha',0.50);
bubblechart(x2,y2, x2/25, "#cb91c0",'MarkerFaceAlpha',0.50);
bubblechart(x3,y3, x3/25, "#f6938c",'MarkerFaceAlpha',0.50);
bubblechart(x4,y4, x4/25, "#4ebd94",'MarkerFaceAlpha',0.50);
bubblechart(x5,y5, x5/25, "#45bced",'MarkerFaceAlpha',0.50);
hold off

xticks([2000 3000 4000 5000])
yticks([10 20 30 40])
bubblesize([2,20]);
xlabel('Weight');
ylabel('MPG');