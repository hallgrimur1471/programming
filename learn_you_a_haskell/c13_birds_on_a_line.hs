import Control.Monad.Error

type Birds = Int
type Pole = (Birds,Birds)

landLeft :: Birds -> Pole -> Either String Pole
landLeft n (l,r)
    | abs ((l + n) - r) < 4 = Right (l + n, r)
    | otherwise             = Left ("Bird unbalance: (" ++ show (l+n) ++ "," ++ show r ++ ")")

landRight :: Birds -> Pole -> Either String Pole
landRight n (l,r)
    | abs (l - (r + n)) < 4 = Right (l, r + n)
    | otherwise             = Left ("Bird unbalance: (" ++ show l ++ "," ++ show (r+n) ++ ")")

-- landRight 2 (0,0) >>= landLeft 2 >>= landRight 2
landAlot :: Either String Pole
landAlot = do
    a <- landRight 2 (0,0)
    b <- landLeft 6 a
    c <- landRight 2 b
    return c
