main :: IO ()
main = do

    putStr "\nDigite o primeiro número: "
    num1 <- readLn :: IO Int

    putStr "\nDigite o segundo número: "
    num2 <- readLn :: IO Int

    putStrLn $ "\nA soma é: " ++ (show (num1 + num2))