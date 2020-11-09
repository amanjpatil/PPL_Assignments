class Animals:
    def __init__(self, legs = 4, eyes=2):
        self.legs = legs
        self.eyes = eyes

class wild_animals(Animals):
    def habitat(self):
        print("Lives in Jungle")

class carnivores(wild_animals):
    def food(self):
        print("Eats Meat")
    
        
class tiger(carnivores):
    def speak(self):
        print("Roars")
    def feature(self):
        print("Tiger has a muscular body with powerful forelimbs, a large head and a tail that is about half the length of its body")
        
class lion(carnivores):
    def speak(self):
        print("Roars")
    def feature(self):
        print("Lions have strong, compact bodies and powerful forelegs, teeth and jaws for pulling down and killing prey")
        
class hyena(carnivores):
    def speak(self):
        print("laughs")
    def feature(self):
        print("The spotted hyena is the largest species, and it grows to 4 to 5.9 feet (1.2 to 1.8 meters) long and\n2.5 to 2.6 feet (77 to 81 centimeters) tall from paw to shoulder.")


                        
class herbivores(wild_animals):
    def food(self):
        print("Eat Plants")

class deer(herbivores):
    def speak(self):
        print("bellow")
    def feature(self):
        print("Deer are often identified with their Horns which is in most Species, is exclusive to the Males only.")
        
class elephant(herbivores):
    def speak(self):
        print("trumpet")
    def feature(self):
        print("Elephants are the largest land animals on Earth, and they're one of the most unique-looking animals")
        
class zebra(herbivores):
    def speak(self):
        print("neigh, whinny, nicker")
    def feature(self):
        print("The most prominent feature of zebras is the bold patterns on their coats.")


class domestic_animals(Animals):
    
    def habitat(self):
        print("Areas habitated by human beings")

        
class dog(domestic_animals):
    def speak(self):
        print("bark")
    def feature(self):
        print("For more than 12,000 years it has lived with humans as a hunting companion, protector,\nobject of scorn or adoration, and friend.")
        
class cat(domestic_animals):
    def speak(self):
        print("meow")
    def feature(self):
        print("The cat is similar in anatomy to the other felid species.\nIt has a strong flexible body,\nquick reflexes, sharp teeth and retractable claws adapted to killing small prey.")
        
class cow(domestic_animals):
    def speak(self):
        print("moo")
    def feature(self):
        print("Domestic cows are one of the most common farm animals around the world")
        
class goat(domestic_animals):
    def speak(self):
        print("bleat, maa")
    def colour(self):
        print("Goat, any ruminant and hollow-horned mammal belonging to the genus Capra.")

my_cat = cat()
my_cat.speak()
my_cat.habitat()
my_cat.feature()
print(my_cat.eyes)
print(my_cat.legs)
my_dog= dog(legs = 5)
my_dog.speak()
my_dog.habitat()
my_dog.feature()
print(my_dog.eyes)
print(my_dog.legs)

