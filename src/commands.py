
import click
import json
from models import db, Person, Planet

file_sample_users = open('src/sample_users_for_commands')
file_sample_planets = open('src/sample_planets_for_commands')
sample_users = json.load(file_sample_users)
sample_planets = json.load(file_sample_planets)

def setup_commands(app):
  
    @app.cli.command("insert-test-planets")
    def insert_test_planets():
        max_count = 2
        print("Creating Star Wars planets) in database...")
        for x in range(0, max_count):
            planet = Planet()
            planet.name = sample_planets[x]["name"],
            planet.terrain = sample_planets[x]["terrain"],
            db.session.add(planet)
            db.session.commit()
            print("Planet: ", planet.name, " created.")

        print("All test planets created")
    

    @app.cli.command("insert-test-persons") 
    @click.argument("count") 
    def insert_test_persons(count):
        print("Creating Star Wars character(s) in database...")
        for x in range(0, int(count)):
            # print(sample_users[x])
            person = Person()
            person.name = sample_users[x]["name"],
            person.homeworld = Planet.query
            db.session.add(person)
            db.session.commit()
            print("Person: ", person.name, " created.")

        print("All test users created")