{-- A professora Jadilene da disciplina de matemática, deseja criar uma ferramenta que facilite a classificação de números especiais para seus alunos. 
Ela sabe que essa ferramenta pode ser uma ótima maneira de despertar o interesse dos alunos pela matemática

Os números especiais em questão são:

- Um número inteiro positivo é considerado um "Numero Perfeito" se a soma dos seus divisores próprios (excluindo ele mesmo) for igual a ele.

- Um número inteiro positivo é considerado um "Numero Abundante" se a soma dos seus divisores próprios for maior do que ele.

- Um número inteiro positivo é considerado um "Numero Deficiente" se a soma dos seus divisores próprios for menor do que ele.

- Um número inteiro não positivo é considerado um "Numero Invalido"

Sua tarefa, é implementar um programa Haskell que recebe um número inteiro N como entrada e determina em qual das categorias acima ele se encaixa. --}


isPositive :: Int -> Bool
isPositive number = number > 0


-- Pode ser feito sem a utilização de list comprehensive
sumDivisors :: Int -> Int
sumDivisors number = do
    
    let allDivisors = [divisors | divisors <- [1..(number `div` 2)], ((\d -> number `mod` d == 0) divisors)]

    sum allDivisors


main :: IO()
main = do

    putStr "\nDigite um número: "

    number <- readLn :: IO Int

    if isPositive number then do

        -- "sum" já é uma função pronta em Haskell e não deve ser usada como variável
        let totalSum = (sumDivisors number)

        if totalSum < number then putStrLn "\nNúmero Deficiente"

        else if totalSum > number then putStrLn "\nNúmero Abundante"

        else putStrLn "\nNúmero Perfeito"        

    else putStrLn "Número Inválido"


{-- Teste Público:

Entrada:
        12

Saída: 
        Número Abundante 

Entrada:
        1

Saída: 
        Número Deficiente

Entrada:
        6

Saída: 
        Número Perfeito
--}
