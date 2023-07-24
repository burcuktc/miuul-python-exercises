#######
#Uygulama
#######

# Verilen bir girdi metni aşağıdaki şekilde değiştiren fonksiyon yazmak istiyoruz.
# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"



#Yöntem 1:

def alternating(string):
    new_string=''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    print(new_string)

alternating('hi my name is john and i am learning python')


#Yöntem 2 (Enumerate ile):
def alternating_with_enumerate(string):
     new_string=''
     for i,letter in enumerate(string):
         if i % 2 == 0:
             new_string+=letter.upper()
         else:
             new_string+=letter.lower()
     print(new_string)

alternating_with_enumerate('hi my name is john and i am learning python')

