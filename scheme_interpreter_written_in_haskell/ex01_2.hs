module Main where
import System.Environment

argSum x y = show $ read x + read y

main :: IO()
main = do
    args <- getArgs
    putStrLn ("Sum = " ++ argSum (args !! 0) (args !! 1))
