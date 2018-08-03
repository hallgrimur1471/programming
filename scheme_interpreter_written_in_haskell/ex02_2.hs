{-
 - Our strings aren't quite R5RS compliant, becuase they don't support escaping
 - of internal quotes within the string. Change parseString so that \" gives a
 - literal quote character instead of terminating the string. You may want to
 - replace noneOf "\"" with a new parser action that accepts either a
 - non-quote character or a backslash followed by a quote mark.

 - Rewrite parseNumber, without liftM, using do-notation
-}

module Main where
import Control.Monad
import System.Environment
import Text.ParserCombinators.Parsec hiding (spaces)

main :: IO()
main = do
    args <- getArgs
    putStrLn (readExpr (args !! 0))

readExpr :: String -> String
readExpr input = case parse parseExpr "lisp" input of
    Left err -> "No match: " ++ show err
--  Right val -> "Found value"
    Right val -> "Found value: " ++ show val

parseExpr :: Parser LispVal
parseExpr = parseAtom
        <|> parseString
        <|> parseNumber

data LispVal = Atom String
             | List [LispVal]
             | DottedList [LispVal] LispVal
             | Number Integer
             | String String
             | Bool Bool deriving(Show)

--ourFilter = do x <- many (noneOf "\"\\")

--charOrEscapedQuote cs = satisfy charOrEscapedQuote

-- str='"as\df"'; ghc --make ex02-2.hs && ./ex02-2 $str
parseString :: Parser LispVal
parseString = do char '"'
                                             #MARK complete this
                 x <- many (noneOf "\"") <|> char "\\" char "\"" many *noneOf
                 char '"'
--                 return $ String x
                 return $ String (x)

parseAtom :: Parser LispVal
parseAtom = do first <- letter <|> symbol
               rest <- many (letter <|> digit <|> symbol)
               let atom = [first] ++ rest
               return $ case atom of
                          "#t" -> Bool True
                          "#f" -> Bool False
--                          _ -> Atom atom
                          otherwise -> Atom atom

parseNumber :: Parser LispVal
parseNumber = do
    rs <- many1 digit
    return $ (Number . read) rs
--parseNumber :: Parser LispVal
--parseNumber = liftM (Number . read) $ many1 digit

symbol :: Parser Char
symbol = oneOf "!$%?*+-/:<=?>@^_~#"

spaces :: Parser ()
spaces = skipMany1 space


