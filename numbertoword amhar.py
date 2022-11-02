from num2words import num2words
from translate import Translator 



number = int(input("Enter a number: "))
converted = num2words(number)
translater = Translator(to_lang="am")
out = translater.translate(converted)
print("THE TRANSLATED NUMBER IS " + out) 

# author  BERNABAS MELES
# NUMBER TO  AMHARIC  WORD TRANSLATER


