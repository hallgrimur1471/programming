data Tree a = Empty | Node a (Tree a) (Tree a) deriving (Show)

freeTree :: Tree Char
freeTree = 
    Node 'P'
        (Node 'O'
            (Node 'L'
                (Node 'N' Empty Empty)
                (Node 'T' Empty Empty)
            )
            (Node 'Y'
                (Node 'S' Empty Empty)
                (Node 'A' Empty Empty)
            )
        )
        (Node 'L'
            (Node 'W'
                (Node 'C' Empty Empty)
                (Node 'R' Empty Empty)
            )
            (Node 'A'
                (Node 'A' Empty Empty)
                (Node 'C' Empty Empty)
            )
        )

changeToP'1 :: Tree Char -> Tree Char
changeToP'1 (Node x l (Node y (Node _ m n) r) = Node x l (Node y (Node 'P' m n) r)

data Direction = L | R deriving (Show)
type Directions = [Direction]

changeToP'2 :: Directions -> Tree Char -> Tree Char
changeToP'2 (L:ds) (Node x l r) = Node Node x (changeToP'2 ds l) r
changeToP'2 (R:ds) (Node x l r) = Node x l (changeToP'2 ds r)
changeToP'2 [] (Node _ l r) = Node 'P' l r

elemAt :: Directions -> Tree a -> a
elemAt (L:ds) (Node _ l _) = elemAt ds l
elemAt (R:ds) (Node _ _ r) = elemAt ds r
elemAt [] (Node x _ _ ) = x

-- let newTree = changeToP [R,L] freeTree
-- elemAt [R,L] newTree

type Breadcrumbs'1 = [Direction]

goLeft'1 :: (Tree a, Breadcrumbs'1) -> Tree a, Breadcrumbs'1)
goLeft'1 (Node _ l _, bs) = (l, L:bs)

goRight'1 :: (Tree a, Breadcrumbs'1) -> (Tree a, Breadcrumbs'1)
goRight'1 (Node _ _ r, bs) = (r, R:bs)

-- go right and then left:
-- goLeft'1 (goRight'1 (freeTree, []))

x -: f = f x

-- go right and then left:
-- (freeTree, []) -: goRight'1 -: goLeft'1

data Crumb a = LeftCrumb a (Tree a) | RightCrumb a (Tree a) deriving (Show)
type Breadcrumbs'2 a = [Crumb a]

goLeft'2 :: (Tree a, Breadcrumbs a) -> (Tree a, Breadcrumbs a)
goLeft'2 (Node x l r, bs) = (l, (LeftCrumb x r):bs)

goRight'2 :: (Tree a, Breadcrumbs a) -> (Tree a, Breadcrumbs a)
goRight'2 (Node x l r, bs) = (r, RightCrumb x l:bs)

goUp'1 :: (Tree a, Breadcrumbs a) -> (Tree a, Breadcrumbs a)
goUp'1 (t, LeftCrumb x r:bs) = (Node x t r, bs)
goUp'1 (t, RightCrumb x l:bs) = (Node x l t, bs)

type Zipper a = (Tree a, Breadcrumbs a)

modify :: (a -> a) -> Zipper a -> Zipper a
modify f (Node x l r, bs) = (Node (f x), l r, bs)
modify f (Empty, bs) = (Empty, bs)

-- go left, then right, then modify root element:
-- let newFocus = modify (\_ -> 'P') (goRight'2 (goLeft'2 (freeTree,[])))
-- or with -:
-- let newFocus = (freeTree,[]) -: goLeft -: goRight -: modify (\_ -> 'P')
-- we can then move up and do a replacement:
-- let newFocus2 = modify (\_ -> 'X') (goUp'1 newFocus)
-- or with -:
-- let newFocus2 = newFocus -: goUp'1 -: modify (\_ -> 'X')

attach :: Tree a -> Zipper a -> Zipper a
attach t (_, bs) = (t, bs)

-- attach a tree to the far left of freeTree:
-- let farLeft = (freeTree,[]) -: goLeft -: goLeft -: goLeft -: goLeft
-- let newFocus = farLeft -: attach (Node 'Z' Empty Empty)

topMost :: Zipper a -> Zipper a
topMost (t,[]) = (t,[])
topMost z = topMost (goUp'1 z)

type ListZipper a = ([a],[a])

goForwards :: ListZipper a -> ListZipper a
goForwards (x:xs, bs) = (xs, x:bs)

goBack :: ListZipper a -> ListZipper a
goBack (xs, b:bs) = (b:xs, bs)

-- A very simple file system

type Name = String
type Data = String
data FSItem = File Name Data | Folder Name [FSItem] deriving (Show)

myDisk :: FSItem
myDisk =
    Folder "root"
        [ File "goat_yelling_like_man.wmv" "baaaaaa"
        , File "pope_time.avi" "god bless"
        , Folder "pics"
            [ File "ape_throwing_up.jpg" "bleargh"
            , File "watermelon_smash.gif" "smash!!"
            , File "skull_man(scary).bmp" "Yikes!"
            ]
        , File "dijon_poupon.doc" "best mustard"
        , Folder "programs"
            [ File "fartwizard.exe" "10gotofart"
            , File "owl_bandit.dmg" "mov eax, h00t"
            , File "not_a_virus.exe" "really not a virus"
            , Folder "source code"
                [ File "best_hs_prog.hs" "main = print (fix error)"
                , File "random.hs" "main = print 4"
                ]
            ]
        ]

data FSCrumb = FSCrumb Name [FSItem] [FSItem] deriving (Show)
type FSZipper = (FSItem, [FSCrumb])

fsUp :: FSZipper -> FSZipper
fsUp (item, FSCrumb name ls rs:bs) = (Folder name (ls ++ [item] ++ rs), bs)

import Data.List (break)

fsTo :: Name -> FSZipper -> FSZipper
fsTo name (Folder folderName items, bs) =
    let (ls, item:rs) = break (nameIs name) items
    in  (item, FSCrumb folderName ls rs:bs)

nameIs :: Name -> FSItem -> Bool
nameIs name (Folder folderName _) = name == folderName
nameIs name (File fileName _) = name == fileName

-- let newFocus = (myDisk,[]) -: fsTo "pics" -: fsTo "skull_man(scary).bmp"
-- fst newFocus
--
-- let newFocus2 = newFocus -: fsUp -: fsTo "watermelon_smash.gif"
-- fst newFocus2

fsNewFile :: FSItem -> FSZipper -> FSZipper
fsNewFile item (Folder folderName items, bs) =
    (Folder folderName (item:items), bs)

-- let newFocus = (myDisk, []) -: fsTo "pics" -: fsNewFile (File "heh.jpg" "lol") -: fsUp

-- Supporting failures

goLeft'3 :: Zipper a -> Maybe (Zipper a)
goLeft'3 (Node x l r, bs) = Just (l, LeftCrumb x r:bs)
goLeft'3 (Empty, _) = Nothing

goRight'3 :: Zipper a -> Maybe (Zipper a)
goRight'3 (Node x l r, bs) = Just (r, RightCrumb x l:bs)
goRight'3 (Empty, _) = Nothing

goUp'2 :: Zipper a -> Maybe (Zipper a)
goUp'2 (t, LeftCrumb x r:bs) = Just (Node x t r, bs)
goUp'2 (t, RightCromb x l:bs) = Just (Node x l t, bs)
goUp'2 (_, []) = Nothing

-- let coolTree = Node 1 Empty (Node 3 Empty Empty)
-- return (coolTree,[]) >>= goRight
-- return (coolTree,[]) >>= goRight >>= goRight
-- return (coolTree,[]) >>= goRight >>= goRight >>= goRight
