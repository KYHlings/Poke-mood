"Pokemon Battle GO!"


class Poketer:
    def __init__(self, name, mood, health, attack):
        self.name = name
        self.mood = mood
        self.health = health
        self.attack = attack

    def __repr__(self):
        return f'Poketer: {self.name} Mood: {self.mood}'


class User:
    def __init__(self, name):
        self.name = name
        self.team = []

    def add_team(self, poketer):
        self.team.append(poketer)

    def __repr__(self):
        return f'Namn: {self.name}, Team: {self.team}'


def main():
    user_pokemon = Poketer("Happy Hasse", "happy", 100, 25)
    cpu_pokemon = Poketer("Aggressive Ada", "angry", 100, 25)

    username = input("Vad heter du? ")
    user = User(username)
    cpu = User("CPU")
    user.add_team(user_pokemon)
    cpu.add_team(cpu_pokemon)
    print(f"Hej {user.name}. Din poketer är {user_pokemon.name}")
    print(f"Din motståndares poketer är {cpu_pokemon.name}\n")
    print(f"{user.name}, det är din tur! ")
    print(f"Välj en stad du tror att det är mycket {user_pokemon.mood} content i.")


    happy_city_dic = {"Göteborg": 25, "Stockholm": 5} #Namn+gläjde
    angry_city_dic = {"Göteborg": 5, "Stockholm": 25}

    city = input("Välj mellan Göteborg eller Stockholm: ")
    print("\nBeräknar mood'content...")

    if city == "Göteborg":
        user_pokemon.health += happy_city_dic["Göteborg"]
        cpu_pokemon.health += angry_city_dic['Stockholm']
        print(f"{user_pokemon.name} valde {city} med mycket happy-content!")
        print(f"Happy Hasse Health increased by {happy_city_dic['Göteborg']}. Total Health: {user_pokemon.health}\n")

        print(f"{cpu_pokemon.name} valde Stockholm med mycket angry-content!")
        print(f"Aggressive Ada Health increased by {angry_city_dic['Stockholm']}. Total Health: {cpu_pokemon.health}\n")

    elif city == "Stockholm":
        user_pokemon.health += happy_city_dic["Stockholm"]
        cpu_pokemon.health += angry_city_dic['Göteborg']
        print(f"{user_pokemon.name} valde {city} med inte så mycket happy-content.")
        print(f"Happy Hasse Health increased by {happy_city_dic['Stockholm']}. Total Health: {user_pokemon.health}\n")

        print(f"{cpu_pokemon.name} valde Göteborg med inte så mycket angry-content.")
        print(f"Aggressive Ada Health increased by {angry_city_dic['Göteborg']}. Total Health: {cpu_pokemon.health}\n")


    print("*** Time to play! ***")
    while True:
        user_choose = int(input("Do you wanna [1] attack or [2] standby?"))
        if user_choose == 1:
            cpu_pokemon.health -= user_pokemon.attack
            print(f"Du ==> Attackerade ==> {cpu_pokemon.name} ")
            print(f"Aggressive Ada now has {cpu_pokemon.health} in health\n")
        elif user_choose == 2:
            print(f"Du =/= Avaktar =/= ")

        if cpu_pokemon.health <= 0:
            print(f'*** Din motståndare svimmade. Du vann! ***')
            break

        user_pokemon.health -= cpu_pokemon.attack
        print(f"{cpu_pokemon.name} ==> Attackerade ==> {user_pokemon.name} ")
        print(f"Your health is now at {user_pokemon.health}\n")
        if user_pokemon.health <= 0:
            print(f'*** Din poketer svimmade. {cpu.name} vann! ***')
            break

if __name__ == '__main__':
    main()