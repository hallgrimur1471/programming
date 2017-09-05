doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y
doubleSmallNumber x = if x > 100
                        then x
                        else x*2
a = [4,8,15,16,32,42]
b = [1,2,3,4] ++ [9,10,11,12]
c = "hello" ++ " " ++ "world"
d = 'A':" SMALL CAT"
e = 5:[1,2,3,4,5]
f = "Steve Buscemi" !! 6
g = [3,4,2] > [3,4]
--h = init last tail head [4,3,2,1]
i = [2,4..20]
j = take 24 [13,26..]
k = take 12 (cycle "LOL ")
l = take 10 (repeat 5)
m = replicate 10 5
n = [x*2 | x <- [1..10]]
o = [ x | x <- [50..100], x `mod` 7 == 3]
boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]
p = [x | x <- [10..20], x /= 13, x /= 15, x /= 19]
q = [ x*y | x <- [2,5,10], y <- [8,10,11]]
length' xs = sum [1 | _ <- xs]
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]
r = [[1,3,5,2,3,1,2,4,5],[1,2,3,4,5,6,7,8,9],[1,2,4,2,1,6,3,1,3,2,3,6]]
s = [ [ x | x <- xs, even x ] | xs <- r]
t = fst ("Wow", False)
u = zip [1..] ["one", "two", "three", "four"]
rightTriangles' = [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a+b+c == 24]
