nom=(input("entrer votre nom"))
prenom=(input("entrer votre prenom"))
postnom=(input("entrer votre postnom "))
age=int(input("entrer votre age"))
if(age<18 and age>0):
    print(f"bonjour{nom}{prenom}{postnom} vous avez{age}ans. vous etes bébé")
elif(age<=18 and age>=0):
    print(f"bonjour{nom}{prenom}{postnom} vous avez{age}ans. vous etes mineur")
elif(age>=18 and age<48):
    print(f"bonjour{nom}{prenom}{postnom} vous avez{age}ans. vous etes majeur")
elif(age>=48 and age<=150):
    print(f"bonjour{nom}{prenom}{postnom} vous avez{age}ans. vous etes vieux")
else:
    print(f"bonjour{nom}{prenom}{postnom} vous avez{age}ans. non identifier")

