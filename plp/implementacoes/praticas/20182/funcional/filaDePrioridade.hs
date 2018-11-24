-- questao http://dirlididi.com/client/index.html#ide/SWdTuSnEO

idosos :: [Int] -> [Int]
idosos lista = [x | x <- lista, x >= 60]

removeIdosos :: [Int] -> [Int]
removeIdosos lista = [x | x <- lista, x < 60]

main :: IO()
main = do
    list <- getLine
    let converted = read list :: [Int]
    putStrLn(show ((idosos converted)++(removeIdosos converted)))