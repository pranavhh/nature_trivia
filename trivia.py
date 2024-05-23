import random
questions = {

    "Level 1": {
      "What is the largest mammal in the world?": {
          "a": "Elephant",
          "b": "Blue Whale",
          "c": "Giraffe",
          "d": "Hippo",
          "answer": "b"
      },
      "Which of the following animals is not a herbivore?": {
          "a": "Rabbit",
          "b": "Lion",
          "c": "Deer",
          "d": "Cow",
          "answer": "b"
      },
      "What gas do plants use during photosynthesis?": {
          "a": "Oxygen",
          "b": "Carbon Dioxide",
          "c": "Nitrogen",
          "d": "Hydrogen",
          "answer": "b"
      },
      "Which of the following is a type of rainforest?": {
          "a": "Taiga",
          "b": "Savanna",
          "c": "Tundra",
          "d": "Amazon",
          "answer": "d"
      },
      "What is the process by which plants make their food?": {
          "a": "Respiration",
          "b": "Photosynthesis",
          "c": "Fermentation",
          "d": "Digestion",
          "answer": "b"
      },

      "Which of these is NOT alive?": {
          "a": "Tree",
          "b": "Rock",
          "c": "Butterfly",
          "d": "Flower",
          "answer": "b"
      },
      "What do plants use to make their food?": {
          "a": "Water",
          "b": "Sunlight",
          "c": "Both a and b",
          "d": "Dirt",
          "answer": "c"
      },
      "What kind of animal lives in the ocean and breathes through gills?": {
          "a": "Snake",
          "b": "Fish",
          "c": "Monkey",
          "d": "Bird",
          "answer": "b"
      },
      "What is the biggest animal on land?": {
          "a": "Elephant",
          "b": "Lion",
          "c": "Giraffe",
          "d": "Bear",
          "answer": "a"
      },
      "What kind of weather brings rain?": {
          "a": "Sunny",
          "b": "Cloudy",
          "c": "Windy",
          "d": "Snowy",
          "answer": "b"
      },
  },
  "Level 2": {
  "What is the baby stage of a frog called?":
  {
   "a": "Tadpole",
   "b": "Pollywog",
   "c": "Newt",
   "d": "Larva",
   "answer": "a"
  },

  "What do decomposers like mushrooms and worms do in nature?": {
    "a": "Break down dead things for nutrients",
   "b": "Help plants grow taller",
   "c": "Catch fish",
   "d": "Fly in the sky",
   "answer": "a",
  },
  "What kind of tree loses its leaves in the fall?":{
    "a": "Evergreen",
   "b": "Deciduous",
   "c": "Palm Tree",
   "d": "Cactus",
   "answer": "b",
  },
   "What is the name of the group of stars that appears to chase the North Star?":{
    "a": "Big Dipper",
    "b": "Little Dipper",
    "c": "Orion",
    "d": "Pleiades",
    "answer": "b"
   },

   "What is the main source of energy for most animals?": {
    "a": "Water",
    "b": "Sunlight",
    "c": "Plants",
    "d": "Minerals",
    "answer": "b"
   },
  "What is the protective outer layer of an insect called?":{
   "a": "Shell",
   "b": "Exoskeleton",
   "c": "Fur",
   "d": "Scales",
   "answer": "b"
  },
  "What is the process by which plants release water vapor into the air?":
  {
   "a": "Photosynthesis",
   "b": "Transpiration",
   "c": "Respiration",
   "d": "Cellular respiration",
   "answer": "b"
  },
  "What is the warm-blooded ocean dweller known for its intelligence?":{
   "a": "Dolphin",
   "b": "Shark",
   "c": "Octopus",
   "d": "Sea turtle",
   "answer": "a"
  },
  "What is the name of the largest desert in the world?":{
   "a": "Gobi Desert",
   "b": "Sahara Desert", 
   "c": "Kalahari Desert",
   "d": "Australian Desert",
   "answer": "b"
  },
 "What is the process by which butterflies emerge from their chrysalis?":{
   "a": "Hibernation",
   "b": "Metamorphosis",
   "c": "Migration",
   "d": "Germination",
   "answer": "b"
 },
 "What is the name of the layer of Earth's atmosphere that protects us from most harmful solar radiation?":{
   "a": "Troposphere",
   "b": "Stratosphere",
   "c": "Mesosphere",
   "d": "Thermosphere", 
   "answer": "b" 
 },
 "What is the main difference between carnivores and herbivores?":{
   "a": "Habitat",
   "b": "Size",
   "c": "Diet",
   "d": "Reproduction",
   "answer": "c"
 },
  "What is the name of the process by which plants absorb water through their roots?":
  {
    "a": "Transpiration",
    "b": "Photosynthesis",
    "c": "Osmosis",
    "d": "Cellular respiration",
    "answer": "c"
  },
   "What is the name of the largest living organism on Earth?":
   {
    "a": "Blue whale",
    "b": "Giant sequoia tree",
    "c": "African elephant",
    "d": "Honey fungus",
    "answer": "b"
   },
    "What is the period of dormancy some animals experience during the winter?":{
      "a": "Hibernation",
    "b": "Migration",
    "c": "Estivation", 
    "d": "Metamorphosis",
    "answer": "a"
    }
}

    
    
}


def ask_question(question, choices):
    print(question)
    for choice, answer in choices.items():
        if choice != "answer":
            print(f"{choice}: {answer}")
    user_answer = input("Your answer (a/b/c/d): ").lower()
    return user_answer
def display_result(correct_answer, user_answer):
    if user_answer == correct_answer:
        print("Excellent! Keep learning about this amazing world!")
        return True
    else:
        print(f"Sorry, the correct answer was {correct_answer.upper()}.")
        return False
def generate_certificate(name, level_tries, level_scores):
    print(f"Congratulations, {name}, you have earned a certificate!")
    print("A downloadable certificate has been generated, detailing your performance.")
def main():
    print (" Welcome to the Nature Trivia Challenge! Get ready to explore the wonders of the natural world across two levels: easy and hard.")
    print  ("Think you have what it takes to become a nature buff?  Let's find out!")
    print ()
    print ("You're venturing into the easy level first. Here, 5 questions await you about the amazing world around us.")
    print("Answer at least 4 correctly, and you'll unlock the challenging second level! Good luck!")
    user_name = input("Enter your name: ")
    level = "Level 1"
    level_score = 0
    total_score = 0
    level_tries = 0
    level_scores = {"Level 1": 0, "Level 2": 0}
    while True:
        for question, choices in random.sample(list(questions[level].items()), 5):
            correct_answer = choices["answer"]
            user_answer = ask_question(question, choices)
            if display_result(correct_answer, user_answer):
                level_score += 1
                total_score += 1
        if level == "Level 1":
            if level_score >= 4:  # Pass Level 1 with 4 or more correct answers
                print("Congratulations! You finished level 1. Let's move to level 2")
                level = "Level 2"
                level_score = 0
                level_tries += 1
                level_scores["Level 1"] = level_score
            else:
                print("You need more practice! Let's try Level 1 again.")
                level_score = 0  # Reset score for retries within the same level
        elif level == "Level 2":
            if level_score >= 3:  # Pass Level 2 with 3 or more correct answers
                generate_certificate(user_name, level_tries, level_scores)
                break
            else:
                print("You almost got it! Let's try Level 2 again.")
                level_score = 0  # Reset score for retries within the same level
        level_tries += 1
        level_scores[level] = level_score
        play_again = input("Do you want to continue to play;? (y/n): ").lower()
        if play_again != "y":
            break
if __name__ == "__main__":
    main()