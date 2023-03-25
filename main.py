# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Console intro to the program

    print("Are we the only habitable planet?")
    print("Until we contact extraterrestrial life, we can analyze 'exoplanets', planets that orbit stars outside of the solar system.")
    print("Considering the planet's details as specified by NASA's exoplanet database, we can predict the likelihood there is life on that planet.")

    # HTTP request to the NASA database for exoplanets

    r = requests.get("https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_masse,ra,dec,sy_dist+from+ps+where+upper(soltype)+like+'%CONF%'+and+pl_masse+between+0.5+and+2.0&format=json")

    # Input choice whether all planets want to be shown or not

    choice = input("Do you want to show all the planets that can be found? (y/n)")

    # Control structure for the choice

    if choice == "y":

        # Iterates through the json array and gets every planet name

        for planet in json.loads(r.text):
            print(planet["pl_name"])
        planetName = input("Pick a planet: ")

        # Uses string that is given for planet and finds the data for the planet

        for wantedPlanet in json.loads(r.text):
            if wantedPlanet["pl_name"] == planetName:
                print(wantedPlanet)
                print("Mass in earths: " + str(wantedPlanet["pl_masse"]))
                print("Radius: " + str(wantedPlanet["ra"]))
                print("Distance from the star in AU: " + str(wantedPlanet["sy_dist"]))

                # Very scientific equation to calculate the probability of life on a planet. Based on the Drake equation, but some factors were taken out
                # Mass in earths divided by the radius of the planet in earths by the distance from their host star

                print("Probability of life: " + str( (wantedPlanet["pl_masse"] / wantedPlanet["ra"] / wantedPlanet["sy_dist"]) * 100 ) + "%")
                break
    elif choice == "n":
        planetName = input("Pick a planet: ")
        for wantedPlanet in json.loads(r.text):
            if wantedPlanet["pl_name"] == planetName:
                print(wantedPlanet)
                print("Mass in earths: " + str(wantedPlanet["pl_masse"]))
                print("Radius: " + str(wantedPlanet["ra"]))
                print("Distance from the star in AU: " + str(wantedPlanet["sy_dist"]))
                print("Probability of life: " + str(
                    (wantedPlanet["pl_masse"] / wantedPlanet["ra"] / wantedPlanet["sy_dist"]) * 100) + "%")
                break




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
