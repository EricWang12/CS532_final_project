load 4dArray.mat
Z = A(:,:,1,:);

Lengths = [188,197,194,198,185,186,194,200,179,203];
b = Z(:,:,:);
%zero = table2array([z{:}]);
digitS = zeros(1024 ,10, 179);

%%

for num = 1:10
    
    for k = 1:179
        Z = A(:,:,num,:);
        if sum(sum(isnan(Z(:,:,k)))) > 0
            continue
        end
        S = reshape( Z(:,:,k), [1024,1]);
        digitS(:,num,k) =  S;
    end
end

save('trainPCA.mat','digitS')

