word_list = [
   "Computador", 
   "Programação", 
   "Desenvolvimento", 
   "Python", 
   "Algoritmo", 
   "Tecnologia", 
   "Software", 
   "Hardware", 
   "MySQL",
]

def bigger_word(word_list):
   bigger = word_list[0]
   for word in word_list:
      if len(word) > len(bigger):
         bigger = word
   return bigger

def minor_word(word_list):
   minor = word_list[0]
   for word in word_list:
      if len(word) < len(minor):
         minor = word
   return minor

print(f"\nA maior palavra da lista é: {bigger_word(word_list)}")
print(f"\nA menor palavra da lista é: {minor_word(word_list)}")