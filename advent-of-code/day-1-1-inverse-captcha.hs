main = do
    inputStr <- getContents
    let numbers = map (\x -> read [x] :: Int) inputStr
    putStrLn . show . inverseCaptcha $ numbers++[head numbers]

inverseCaptcha (x:y:ys)
    | x==y      = x + inverseCaptcha (y:ys)
    | otherwise = inverseCaptcha (y:ys)
inverseCaptcha _ = 0
