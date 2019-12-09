d = dir('*.txt');
N=length(d);     % how many did we find?
A=zeros(32,N);   % allocate for 24 points of data 1 column/file

for k = 1 : length(d)   
    M=dlmread(d(k).name)
end