import System.IO
import Data.Char

main = do
    withFile' "magnusopum.txt" ReadMode (\handle -> do
        contents <- hGetContents handle
        putStr $ map toUpper contents)

-- type FilePath = String

withFile' :: FilePath -> IOMode -> (Handle -> IO a) -> IO a
withFile' filePath mode handleFunc = do
    handle <- openFile filePath mode
    result <- handleFunc handle
    hClose handle
    return result
