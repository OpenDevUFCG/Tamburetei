{-- Maria está planejando sair com suas amigas no fim de semana, mas está indecisa sobre seu traje. 

Auxilie Maria ao exibir todas as potenciais combinações de roupas que ela pode usar, desenvolvendo um programa para isso. 
O programa receberá dois conjuntos de roupas como entrada e produzirá todas as combinações viáveis a partir desses conjuntos. --}

combinations :: [String] -> [String] -> [String]
combinations [] _ = []
combinations (u:ut) lowerClothes = map (\y -> u ++ " e " ++ y) lowerClothes ++ (combinations ut lowerClothes)


main :: IO()
main = do

    putStr "\nDigite o primeiro conjunto de roupas: "
    firstOption <- getLine

    putStr "\nDigite o segundo conjunto de roupas: "
    secondOption <- getLine
    
    let upperClothes = words firstOption
    let lowerClothes = words secondOption

    putStrLn "\nAs combinações possíveis são:\n"

    mapM_ putStrLn $ combinations upperClothes lowerClothes


{-- Teste Público:

Entrada:
       BlusaAzul CasacoPreto RegataAmarela
       CalçaJeans SaiaRosa

Saída:	
       BlusaAzul e CalçaJeans
       BlusaAzul e SaiaRosa
       CasacoPreto e CalçaJeans
       CasacoPreto e SaiaRosa
       RegataAmarela e CalçaJeans
       RegataAmarela e SaiaRosa 
--}