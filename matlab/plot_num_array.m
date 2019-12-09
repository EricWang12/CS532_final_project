function [checker_plot] = plot_num_array(arr)
%PLOT_NUM_ARRAY Plot the 32 by 32 array on a checkerboard plot
%   Use pcolor to plot and fill the checkerboard plot

[h, w] = size(arr);
arr = [arr zeros(h, 1); zeros(1, w+1)];
checker_plot = pcolor(arr);
colormap(gray(2))
axis ij
axis square
end

