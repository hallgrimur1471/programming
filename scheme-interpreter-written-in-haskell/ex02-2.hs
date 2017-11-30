{-
 - Our string aren't quite R5RS compliant, becuase they don't support escaping
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
    Right val -> "Found value: " ++ show val

parseExpr :: Parser LispVal
parseExpr = parseString
        <|> parseAtom
        <|> parseNumber

data LispVal = Atom String
             | List [LispVal]
             | DottedList [LispVal] LispVal
             | Number Integer
             | String String
             | Bool Bool deriving(Show)

ourFilter = do x <- many (noneOf "\"\\")

charOrEscapedQuote cs = satisfy charOrEscapedQuote

parseString :: Parser LispVal
parseString = do char '"'
                 x <- ourFilter
                 x <- many (noneOf "\"")
                 char '"'
                 return $ String x

parseAtom :: Parser LispVal
parseAtom = do first <- letter <|> symbol
               rest <- many (letter <|> digit <|> symbol)
               let atom = [first] ++ rest
               return $ case atom of
                          "#t" -> Bool True
                          "#f" -> Bool False
                          otherwise -> Atom atom

parseNumber :: Parser LispVal
parseNumber = do
    rs <- many1 digit
    return $ (Number . read) rs

symbol :: Parser Char
symbol = oneOf "!$%?*+-/:<=?>@^_~#"

spaces :: Parser ()
spaces = skipMany1 space


