import Data.Char

main = do
    putStr "Write a polish expression: "
    input <- getLine
    putStrLn $ show $ calculatedResult input
    main

-- calculatedResult :: (Num a, Read a) => String -> a
calculatedResult :: String -> Float
calculatedResult expression =
    let wordList = words expression
    in  head $ foldl morphStack [] wordList

-- morphStack :: (Num a, Read a) => [a] -> String -> [a]
morphStack :: [Float] -> String -> [Float]
morphStack (x:y:ys) "+" = (y + x):ys
morphStack (x:y:ys) "-" = (y - x):ys
morphStack (x:y:ys) "*" = (y * x):ys
morphStack (x:y:ys) "/" = (y / x):ys
morphStack (x:y:ys) "^" = (y ** x):ys
morphStack (x:xs) "ln" = log x:xs
morphStack xs "sum" = [sum xs]
morphStack xs numberString = read numberString:xs

