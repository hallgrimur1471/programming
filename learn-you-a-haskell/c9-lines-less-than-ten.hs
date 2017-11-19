main = do
    contents <- getContents
    putStr $ linesLessThanTen contents

linesLessThanTen :: String -> String
linesLessThanTen input =
    let allLines = lines input
        shortLines = filter (\line -> length line < 10) allLines
    in unlines shortLines
