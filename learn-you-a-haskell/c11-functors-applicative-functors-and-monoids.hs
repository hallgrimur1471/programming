import qualified Data.Foldable as F

newtype Any = Any { getAny :: Bool }
    deriving (Eq, Ord, Read, Show, Bounded)

instance Monoid Any where
    mempty = Any False
    Any x `mappend` Any y = Any (x || y)

data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

instance F.Foldable Tree where
    foldMap f Empty = mempty
    foldMap f (Node x l r) = F.foldMap f l `mappend`
                             f x           `mappend`
                             F.foldMap f r

testTree = Node 5 (Node 3 (Node 1 Empty Empty) (Node 6 Empty Empty) ) (Node 9 (Node 8 Empty Empty) (Node 10 Empty Empty) )

a = F.foldl (+) 0 testTree
b = F.foldl (*) 1 testTree
c = getAny $ F.foldMap (\x -> Any $ x == 3) testTree
d = getAny $ F.foldMap (\x -> Any $ x > 15) testTree
e = F.foldMap (\x -> [x]) testTree
