{-- Paulo foi em uma padaria e quer saber o valor da sua conta. 
Para ajudá-lo, faça um programa que receba a quantidade de itens consumidos, 
uma descrição dos itens e retorna o valor da conta.

Cardápio:

cafe            R$ 4
pao             R$ 2
suco            R$ 5
pao de queijo   R$ 5
sanduiche       R$ 3
--}

valorDoItem :: String -> Int
valorDoItem item 

    | item == "cafe" = 4
    | item == "pao" = 2
    | item == "suco" = 5
    | item == "pao de queijo" = 5 
    | item == "sanduiche" = 3
    | otherwise = 0


lerItens :: Int -> Int -> IO Int
lerItens 0 soma = return soma
lerItens n soma = do

    item <- getLine

    let somaAtualizada = soma + (valorDoItem item)

    lerItens (n-1) somaAtualizada


main :: IO()
main = do

    putStr $ "\nCardápio:\n"
          ++ "          Café, Pão, Suco, Pão de Queijo, Sanduiche\n"
          ++ "\nDigite a quantidade de itens: "

    numeroDeItens <- readLn :: IO Int

    putStrLn "\nDigite as opções escolhidas, sequencialmente, (sem acento e todo em minúsculo):\n"

    valorDaCompra <- (lerItens numeroDeItens 0)

    putStrLn $ "\nO valor total da compra é: " ++ show (valorDaCompra) ++ " reais"

    
-- Teste Público:

-- Entrada:
--              5

--              cafe

--              pao

--              suco

--              cafe

--              sanduiche

-- Saída: 
--              18