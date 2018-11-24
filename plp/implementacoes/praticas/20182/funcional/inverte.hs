-- questao http://dirlididi.com/client/index.html#ide/PtXk9iuGG

inverte :: String -> String
inverte [] = []
inverte (h:t) = inverte(t) ++ [h]

funcao :: String -> String -> String
funcao l [] = []
funcao l (h:t) | [h] == l = [h] ++ inverte t
            | otherwise = [h] ++ funcao l t

main :: IO()
main = do
    l <- getLine
    list <- getLine
    putStrLn( funcao l list) 