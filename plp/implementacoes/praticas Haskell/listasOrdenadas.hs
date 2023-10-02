{-- Crie um programa em Haskell que receba uma lista de números inteiros e retorne duas sublistas: 
uma contendo os números ímpares em ordem crescente e outra contendo os números pares em ordem decrescente.

ATENÇÃO: Você não deve usar funções prontas de que ordenem listas!! --}

-- | QuickSort
orderedList :: [Int] -> [Int]
orderedList [] = []
orderedList (x:xs) =
    let smallers = orderedList [s | s <- xs, s <= x]
        biggers = orderedList [b | b <- xs, b > x]
    in smallers ++ [x] ++ biggers
    
-- | Ordem crescente dos elementos ímpares 
ascendingOddList :: [Int] -> [Int]
ascendingOddList [] = []
ascendingOddList list = [x | x <- list, not (even x)]

-- | Ordem decrescente dos elementos pares 
descendingEvenList :: [Int] -> [Int]
descendingEvenList [] = []
descendingEvenList list = reverse [x | x <- list, even x]


main :: IO()
main = do

    putStr "\nDigite a lista de números: "

    strList <- getLine
    
    let list = (map read (words strList)) :: [Int]
    let inOrder = (orderedList list)
    
    putStrLn $ "\nNúmeros ímpares em ordem crescente: " ++ show (ascendingOddList inOrder) ++ "\n"
            ++ "\nNúmeros pares em ordem decrescente: " ++ show (descendingEvenList inOrder)
            
            
{-- Teste Público:

Entrada:

    1 2 3 4 5 6 7 8 9

Saída:

    Números ímpares em ordem crescente: [1,3,5,7,9]

	Números pares em ordem decrescente: [8,6,4,2] 
--}

