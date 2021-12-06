class Eroare(Exception):
  pass



try:
  n = int(input("Dati numarul natural: "))
  
  if (n<0):
    raise Exception
  
  if (n>5 and n<8):
    raise Eroare("numar intre 20")
  
except ValueError:
  print ("Nu ati inserat un numar.")

except Eroare as ve:
  print(str(ve))

except Exception:
  print("Numarul nu este natural.")
