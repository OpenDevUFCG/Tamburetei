--- FUNÇÃO SPLIT QUE GERA UMA LISTA DE STRING ---
wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

--- GERA UMA LISTA DE LISTA SEM A LISTA QUE CONTEM O STRING PASSADO COMO PARÂMETRO ---
geraLista :: String -> [[String]] -> [[String]]
geraLista _ [] = []
geraLista v (x:xs) | (aux v x) == True = geraLista v xs
                   | otherwise = x:geraLista v xs

aux :: String -> [String] -> Bool
aux v (x:xs) = (v == x)

--- RECEBE UM PARÂMETRO E O ESCREVE NO ARQUIVO .txt ---
--- NECESSÁRIO IMPORTAR O System.IO ---
escreveArquivo :: String -> IO()
escreveArquivo n = do

    arq <- openFile "nomeArquivo.txt" WriteMode
    hPutStr arq n
    hFlush arq
    hClose arq

