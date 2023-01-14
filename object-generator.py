from datetime import datetime, timedelta
from typing import List
import random
import argparse
import json

def generate_objects(duration: int, min_rate: int, max_rate, colours: List):
    timestamp = datetime.now()
    object_id = 0
    while duration != 0:
        for i in range(0,random.randint(min_rate, max_rate)):
            colour = random.choice(colours)
            object ={   "id": object_id,
                        "colour": colour,
                        "timestamp": str(timestamp)}
            yield object
            object_id += 1
        timestamp += timedelta(seconds=1)
        duration -= 1

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-config")
    args = parser.parse_args()

    with open(args.config) as config_file:
        config = json.load(config_file)
        duration = config["duration"]
        colours = config["colour"]["values"]
        min_rate = config["rate"]["min"]
        max_rate = config["rate"]["max"]
        print(colours, duration, min_rate, max_rate)

        for object in generate_objects(duration, min_rate, max_rate, ["blue", "green"]):
            print(object)
