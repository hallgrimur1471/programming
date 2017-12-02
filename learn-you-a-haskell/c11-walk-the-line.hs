type Birds = Int
type Pole = (Birds, Birds)

landLeft :: Birds -> Pole -> Maybe Pole
landLeft n (left, right) =
    | abs ((left + n) - right) < 4 = Just (left + n, right)
    | otherwise                    = Nothing

landRight :: Birds -> Pole -> Pole
landRight n (left, right) =
    | abs (left - (right + n)) < 4 = (left, right + n)
    | otherwise                    = Nothing

x -: f = f x
-- (0,0) -: landRight 2 -: landLeft 2 -: landRight 2
-- (2,4)
--
-- (0,0) -: landLeft 1 -: landRight 4 -: landLeft (-1) -: landRight (-2)
-- (0,2)
--
--
-- return (0,0) >>= landRight 2 >>= landLeft 2 >>= landRight 2
-- Just (2,4)
--
-- return (0,0) >>= landLeft 1 >>= landRight 4 >>= landLeft (-1) >>= landRight (-2)
-- Nothing

banana :: Pole -> Maybe Pole
banana _ = Nothing
