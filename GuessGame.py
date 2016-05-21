import random
max_num = 10
secret_num = random.randint(1, max_num)
print("Ich denke eine nummer zwischen 1 bis " + str(max_num) + "...")

max_vermutungen = 3
vermuten_ubrig = max_vermutungen
while vermuten_ubrig:
  print("Denken ubrig: " + str(vermuten_ubrig))
  vermuten = int(input("Schreiben Sie die antwort hier: "))
  if vermuten == secret_num:
    print("Korrekt!!! Sie gewonnen")
    break
  elif vermuten < secret_num:
    print("Das ist zu niedrig.")
  else:
    print("Das ist zu hoch.")
    vermuten_ubrig -= 1
else:
  print("Sorry, Sie sind aus Vermutungen.")
