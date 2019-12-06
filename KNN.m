clear all;
close all;

load fisheriris
x = meas(:,3:4);
gscatter(x(:,1),x(:,2),species)
legend('Location','best')

NumNeighbors = 20;
newpoint = [5 2];


line(newpoint(1),newpoint(2),'marker','x','color','k',...
   'markersize',10,'linewidth',2)

Mdl = KDTreeSearcher(x);
[n,d] = knnsearch(Mdl,newpoint,'k',NumNeighbors);
line(x(n,1),x(n,2),'color',[.5 .5 .5],'marker','o',...
    'linestyle','none','markersize',10)

ctr = newpoint - d(end);
diameter = 2*d(end);
% Draw a circle around the 10 nearest neighbors.
h = rectangle('position',[ctr,diameter,diameter],...
   'curvature',[1 1]);
h.LineStyle = ':';
daspect([1 1 1])    %force the axis to be 1:1

tabulate(species(n))