# Bobina de Papel

Implemente o circuito de controle do mecanismo para troca de bobinas de papel de uma máquina de impressão rotativa. O uso desse tipo de máquina é comum em jornais e revistas, onde são necessárias bobinas de papel com mais de 1 metro de largura e diâmetro.

Em máquinas de impressão rotativa, o papel passa em alta velocidade e, quando uma bobina está acabando, a nova deve ser colocada sem parar ou desacelerar o processo de impressão. Para isso, a nova bobina deve ser inserida e colocada em rotação, de modo que possa ser colada à bobina antiga. Após a colagem, uma grande lâmina corta o papel da bobina que está se esgotando.

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[7] |
| `nova` | SWI[0] |
| `velocidade` | SWI[1] |
| `vazio` | SWI[2] |

- O `reset` deve ser síncrono.
- O `clock` deve ter frequência de 1 Hz.
- A `nova` indica que uma nova bobina já se encontra dentro da máquina de impressão rotativa.
- A `velocidade` indica que a nova bobina já se encontra na velocidade adequada para a colagem.
- O `vazio` indica que a bobina antiga está vazia.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `acelerar` | LED[0] |
| `colar` | LED[1] |
| `cortar` | LED[2] |
| `alarme` | LED[3] |

- O `acelerar` indica que o motor para aceleração da nova bobina está ligado.
- O `colar` indica que o dispositivo que cola as duas bobinas está ativado.
- O `cortar` indica que o dispositivo que corta o papel da bobina antiga está ativado.
- O `alarme` indica a ocorrência de condições anormais.

## Descrição

- Após o `reset`, o motor de aceleração de bobina, o alarme e os dispositivos de colagem e corte são desativados.

- Quando o papel de uma bobina está acabando, se não já houver uma nova bobina inserida na máquina, o alarme é ativado. Se houver, essa nova bobina deve ser acelerada até atingir a velocidade correta.

- A velocidade correta de rotação da nova bobina deve ser atingida em mais do que 1 e menos do que 4 ciclos de *clock*. Se isso não ocorrer, o alarme é ativado e o motor de aceleração é desligado.

- Quando a velocidade correta da nova bobina for atingida, o motor deve ser desligado e o dispositivo de colagem deve ser ativado durante exatamente 1 ciclo de *clock*. Em seguida, o dispositivo de corte deve ser acionado durante exatamente 1 ciclo de *clock*.

- Se durante os procedimentos descritos acima a bobina ficar vazia, o alarme deve ser ativado, desligando o motor e os dispositivos de colagem e corte.

- Se o alarme não foi ativado até esse ponto da operação, a bobina antiga está agora no lugar onde deve ser inserida a nova bobina. Assim, a chave `nova` deve ser desativada e reativada num intervalo de 3 ciclos de *clock*, sinalizando a remoção da bobina antiga e a inserção de uma nova. Se isso não ocorrer, o alarme deve ser acionado. Caso contrário, a operação se repete.

- Depois de ativado, o alarme permanece assim até que o circuito da máquina de impressão sofra *reset*.