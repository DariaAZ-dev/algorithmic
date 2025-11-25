import tpa.collatz as co  # import et définition (optionnelle) d'alias

seed: int = 1999
index: int = co.collatz_lifetime(seed)
series: list[int] = co.collatz_series(seed, index)
height: int = co.collatz_altitude(seed)

print(f"La suite de Collatz pour N={seed} "
      f"a une durée de vie de {index}, une altitude de {height}\n"
      f"et ses premiers termes sont {series[:10]}"
)
