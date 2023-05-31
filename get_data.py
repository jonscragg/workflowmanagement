"""
This module contains functions for reading data and validating it.
Author: paarthsanhotra@gmail.com
Date: 11-04-2023
"""

import csv
import json
from pymongo import MongoClient
import collections
from pathlib import Path

recipes = []


def create_experiment():
    """Creates a dictionary of experiments."""
    filename = Path("data/experiments.json")
    with open(filename, "r") as f:
        experiments = json.load(f)
    experiments_to_delete = []
    for experiment in zip(experiments, experiments.values()):
        if not verify_experiment(experiment):
            print(experiment[1]["recipe_name"], "is not a valid experiment.")
            experiments_to_delete.append(experiment[0])

    for experiment in experiments_to_delete:
        del experiments[experiment]

    return experiments


def create_recipes():
    """Reads a csv file and creates a list of recipes."""
    filename = Path("data/recipes.csv")
    with open(filename, "r") as f:
        reader = csv.reader(f)
        result = [[item for item in row if item != ""] for row in reader]
        for row in result:
            recipes.append(row)
    return recipes


def verify_experiment(experiment):
    """Verifies if an experiment is valid."""
    for number in range(len(recipes)):
        if (
            experiment[1]["recipe_name"] in recipes[number][0]
            and len(experiment[1]["parameters"]) == len(recipes[number]) - 1
        ):
            parameters = [item for item in experiment[1]["parameters"]]
            return collections.Counter(parameters) == collections.Counter(
                recipes[number][1:]
            )


# connect to mongodb
def connect_mongo():
    # insert the connection string for mongo db
    client = MongoClient(
        "mongodb+srv://user123:Paarth12345@cluster0.7sgpqhl.mongodb.net/?retryWrites=true&w=majority"
    )

    # create database
    db = client["column_headings"]
    print(db)
    # create collection
    collection = db["columns"]
    print(collection)
    new_data = create_experiment()
    collection.insert_one(new_data)
    print(collection)

    print(client.list_database_names())
    # print(client.server_info())


if __name__ == "__main__":
    create_recipes()
    create_experiment()


if __name__ != "__main__":
    create_recipes()
