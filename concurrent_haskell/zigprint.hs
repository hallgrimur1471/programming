-- ghc --make zigprint.hs && ./zigprint
import Control.Concurrent

main = do
    forkIO (loop "yes ")
    loop "nope! "

loop ch = do
    putStr ch
    loop ch
