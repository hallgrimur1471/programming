import Control.Applicative
import Data.List.Split

main = do
    inputStr <- getContents
    let lines = splitOn "\n" inputStr
    let rows = map (\line -> map (\x -> read x :: Int) (splitOn "\t" line)) lines
    let divsum = sum $ map (\line -> sum $ maybeDivision <$> line <*> line) rows
    putStrLn $ show divsum

maybeDivision x y
    | x==y = 0
    | x `mod` y == 0 = x `div` y
    | otherwise = 0
