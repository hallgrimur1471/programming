import Control.Applicative

main = do
    inputStr <- getContents
    let numbers = map (\x -> read [x] :: Int) inputStr
    putStrLn $ answer numbers 

answer numbers = case split numbers of
    Left err  -> show err
    Right val -> show $ inverseCaptcha (fst val) (snd val)

inverseCaptcha x y = (*2) . sum . getZipList $ numIfEqual <$> ZipList x <*> ZipList y

numIfEqual a b
    | a==b      = a
    | otherwise = 0

split xs
    | even $ length xs = Right (l,r)
    | otherwise = Left error
    where error = "Split does not support lists of uneven length"
          half = length xs `div` 2
          l = take half xs
          r = drop half xs

-- simple version:

--main = do
--    inputStr <- getContents
--    let numbers = map (\x -> read [x] :: Int) inputStr
--    let half = length numbers `div` 2
--    let left = take half numbers
--    let right = drop half numbers
--    putStrLn $ show . (*2) . sum $ map (\t -> fst t) $ filter (\t -> fst t == snd t) $ zip left right
