{-- A professora de matemática, Jadilene, está animada para introduzir um conceito fascinante aos seus alunos: a sequência especial. 
Ela acredita que essa sequência numérica possui propriedades únicas.

A sequência especial começa com o número 2 e, a partir do segundo termo, cada termo é a soma do dobro do termo anterior somado 2. 
Ou seja, a sequência começa: 2, 6, 14, 30, ...

Sua missão, é ajudá-la a implementar um programa em Haskell que recebe um número inteiro N como entrada e 
calcula o N-ésimo termo dessa sequência especial. --}


-- Pode-se usar casamento de padrões ou guardas
-- Pode-se usar uma função lambda ou criar uma função que duplica e soma 2
somaDobro :: Int -> Int -> Int
somaDobro 1 termo = termo
somaDobro n termo = do somaDobro (n - 1) ((\t -> (t * 2) + 2) termo)


main :: IO()
main = do

    putStr "\nDigite a quantidade de termos: "

    quantidadeTermos <- readLn :: IO Int

    if quantidadeTermos < 1 then putStrLn "\nEntrada Inválida!"

    else putStrLn $ "\nA soma da sequência especial é: " ++ show (somaDobro quantidadeTermos 2)


{-- Teste Público:

Entrada: 
3

Saída:
14 --}