#Junior Silva - 120110464
#UFCG
j = 1
soma = 0.2
n = i = 0

while i <= 2:
    for c in range(1, 4):
        if i > 2.19:
            print(f"I={2:.0f} J={j:.0f}")
        if i == 0.0 or i == 1.0 or i > 1.8:
            print(f"I={i:.0f} J={j:.0f}")
        elif i < 2:
            print(f"I={i:.1f} J={j:.1f}")
        j = j + 1
    i = i + soma
    j = 1 + i
