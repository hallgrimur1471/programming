factorial 0 = 1
factorial n = n * factorial (n-1)

head' [] = error "Can't call head on an empty list, dummy!"
head' (x:_) = x

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs
