{-- Maria é professora de matemática e gostaria de saber a quantidade de vezes que cada número é sorteado em uma lista
de números aleatórios gerados por um programa de loteria.

Ela deseja que você crie um programa em Haskell que recebe uma lista de números inteiros aleatórios e retorna a
quantidade de vezes que cada número foi sorteado. --}

sorteio :: [String] -> String
sorteio [] = ""
sorteio (x:xs) = x ++ " foi sorteado " ++ show (length [(y:ys) | (y:ys) <- (x:xs), [y] == x]) 
                   ++ " vez(es)\n" ++ sorteio ([(z:zs) | (z:zs) <- (x:xs), [z] /= x])

main :: IO()
main = do

    putStr "\nDigite a lista de números separada por espaço: "
    listaEntrada <- getLine

    let lista = (words listaEntrada)

    putStr $ "\n" ++ (sorteio lista)

-- Teste Público:

-- Entrada:
--          4 7 2 4 8 4 7 9 2 2
-- Saída:
--          4 foi sorteado 3 vez(es)
--          2 foi sorteado 3 vez(es)
--          7 foi sorteado 2 vez(es)
--          8 foi sorteado 1 vez(es)
--          9 foi sorteado 1 vez(es)