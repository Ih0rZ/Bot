import datetime
from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.power = randint(30,70)
        self.hp = randint(100,250)

        self.last_feed = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]["official-artwork"]['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/shiny/1.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
        Сила покемона: {self.power}
        Сила покемона: {self.hp}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
        if chance == 1:
            return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    
    class Wizard(Pokemon):
        def info(self):
            return 'У тебя покемон волшебник'+ super().info()
    
    class Fighter(Pokemon):
        def attack(self, enemy):
            super_power = randint(5,15)
            self.сила += super_power
            result = super().attack(enemy)
            self.сила -= super_power
            return результат + f"\nБоец применил супер-атаку силой:{super_power} "
    def info(self):
        return 'У тебя покемон боец'+ super().info()
    

    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    
    print(fighter.info())
    
    print(fighter.attack(wizard))
    print(wizard.attack(fighter))



    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.current()  
        delta_time = timedelete(hours=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"

