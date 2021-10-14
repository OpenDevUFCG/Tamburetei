--- FUNÇÃO SPLIT QUE GERA UMA LISTA DE STRING ---
--- wordsWhen(==' ') "A OpenDev eh muito massa" RESUTLADO -> ["A","OpenDev","eh","muito","massa"] ---
--- wordsWhen(==',') "1, 2, 3, 4, 5" RESULTADO -> ["1"," 2"," 3"," 4"," 5"] ---
--- FAZ O SPLIT DE ACORDO COM O PARÂMETRO ---
wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

--- GERA UMA LISTA DE LISTA SEM A LISTA QUE CONTEM O STRING PASSADO COMO PARÂMETRO ---
--- geraLista "111" [["111", "Guilherme"], ["222", "Fulano"]] ---
--- RESULTADO -> [["222","Fulano"], ["333","Sicrano"]] ---
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

