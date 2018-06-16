import Data.List.Split

main = do
    inputStr <- getContents
    let lines = splitOn "\n" inputStr
    let rows = map (\line -> map (\x -> read x :: Int) (splitOn "\t" line)) lines
    let checksum = sum $ map (\line -> (maximum line) - (minimum line)) rows
    putStrLn $ show checksum
