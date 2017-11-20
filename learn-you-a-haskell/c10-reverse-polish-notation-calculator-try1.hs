import Data.Char

main = do
    putStr "Write a polish expression: "
    input <- getLine
    putStrLn $ show $ calculatedResult input
    main

calculatedResult :: [Char] -> Int
calculatedResult input =
    let wordList = words input
        foldl morphStack  [] wordList

morphStack :: [String] -> Char -> [String]
morphStack stack element:_  
    | isDigit (read element) = element:stack
    | otherwise = element 
