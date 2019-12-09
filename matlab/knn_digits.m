load trainPCA.mat
load 4dArray.mat
x = digitS(:,:)';

trainData = A(:,:,1:179);

digit = zeros(1790,1);
for k = 1:1790
    digit(k) = ceil(k/179)-1;
end

dimension = 1;

Mdl = KDTreeSearcher(x);

newpoint = A(:,:,7,78);
%[U,S,V] = svd(newpoint);
newpoint = reshape(newpoint, [1024,1]);
[n,d] = knnsearch(Mdl,newpoint,'k',20);


tabulate(digit(n))
