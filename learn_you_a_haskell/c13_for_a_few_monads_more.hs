import Control.Monad.Writer

gcd' :: Int -> Int -> Writer [String] Int
gcd' a b
    | b == 0 = do
        tell ["Finished with" ++ show a]
        return a
    | otherwise = do
        tell [show a ++ " mod " ++ show b ++ " = " ++ show (a `mod` b)]
        gcd' b (a `mod` b)

newtype DiffList a = DiffList { getDiffList :: [a] -> [a] }

toDiffList :: [a] -> DiffList a
toDiffList xs = DiffList (xs++)

fromDiffList :: DiffList a -> [a]
fromDiffList (DiffList f) = f []

instance Monoid (DiffList a) where
    mempty = DiffList (\xs -> [] ++ xs)
    (DiffList f) `mappend` (DiffList g) = DiffList (\xs -> f (g xs))

-- fromDiffList (toDiffList [1,2,3,4] `mappend` toDiffList [1,2,3])

gcdReverse :: Int -> Int -> Writer (DiffList String) Int
gcdReverse a b
    | b == 0 = do
        tell (toDiffList ["Finished with " ++ show a])
        return a
    | otherwise = do
        result <- gcdReverse b (a `mod` b)
        tell (toDiffList [show a ++ " mod " ++ show b ++ " = " ++ show (a `mod` b)])
        return result

finalCountDown :: Int -> Writer (DiffList String) ()
finalCountDown 0 = do
    tell (toDiffList ["0"])
finalCountDown x = do
    finalCountDown(x-1)
    tell (toDiffList [show x])

-- mapM_ putStrLn . fromDiffList . snd . runWriter $ finalCountDown 500000

finalCountDownSlow :: Int -> Writer [String] ()
finalCountDownSlow 0 = do
    tell ["0"]
finalCountDownSlow x = do
    finalCountDownSlow (x-1)
    tell [show x]

-- mapM_ putStrLn . snd . runWriter $ finalCountDownSlow 500000

type Stack = [Int]

pop :: Stack -> (Int,Stack)
pop (x:xs) = (x,xs)

push :: Int -> Stack -> ((),Stack)
push a xs = ((),a:xs)

stackManip :: Stack -> (Int, Stack)
StackManip stack = let
    ((),newStack1) = push 3 stack
    (a, newStack2) = pop newStack1
    in pop newStack2

-- stackManip [5,8,2,1]

-- and now with the State monad

import Control.Monad.State

pop :: State Stack Int
pop = State $ \(x:xs) -> (x,xs)

push :: Int -> State Stack ()
push a = State $ \xs -> ((),a:xs)

stackManip :: State Stack Int
stackManip = do
    push 3
    a <- pop
    pop

stackManip :: State Stack Int
stackManip = do
    push 3
    pop
    pop

import System.Random

randomSt :: (RandomGen g, Random a) => State g a
randomSt = State random

threeCoins :: State StdGen (Bool,Bool,Bool)
threeCoins = do
    a <- randomSt
    b <- randomSt
    c <- randomSt
    return (a,b,c)

-- runState threeCoins (mkStdGen 33)

-- liftM (*3) (Just 8)
-- fmap  (*3) (Just 8)

import Control.Monad

powerset :: [a] -> [[a]]
powerset xs = filterM (\x -> [True, False]) xs

import Data.List
  
inMany :: Int -> KnightPos -> [KnightPos]
inMany x start = return start >>= foldr (<=<) return (replicate x moveKnight)

import Data.Ratio

newtype Prob a = Prob { getProb :: [(a,Rational)] } deriving Show

-- it makes sense to map over Prob since it is a list of things. Let's make
-- Prob an instance of Functor
instance Functor Prob where
    fmap f (Prob xs) = Prob $ map (\(x,p) -> (f x,p)) xs

-- m >>= f always equals join (fmap f m)
-- so we need to figure out how to flatten a nested probability list,
-- then we can write the >>= function
flatten :: Prob (Prob a) -> Prob a
flatten (Prob xs) = Prob $ concat $ map multAll xs
    where multAll (Prob innerxs,p) = map (\(x,r) -> (x,p*r)) innerxs

-- now we have all that we need, we can write the Monad instance!
instance Monad Prob where
    return x = Prob [(x,1%1)]
    m >>= f = flaten (fmap f m)
    fail _ = Prob []

data Coin = Heads | Tails deriving (Show, Eq)

coin :: Prob Coin
coin = Prob [(Heads,1%2),(Tails,1%2)]

loadedCoin :: Prob Coin
loadedCoin = Prob [(Heads,1%10),(Tails,9%10)]

import Data.List (all)

flipThree :: Prob Bool
flipThree = do
    a <- coin
    b <- coin
    c <- loadedCoin
    return (all (==Tails) [a,b,c])
