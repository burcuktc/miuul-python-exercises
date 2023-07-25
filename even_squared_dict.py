# Amaç: Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Key'ler orjinal değerler, value'lar ise değiştirilmiş değerler olacaktır.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

new_dict

#2. yol (dict comprehensions)
{n: n**2 for n in numbers if n % 2 == 0}

