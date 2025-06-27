from art import logo, vs
import random
from game_data import data

print(logo)

score = 0
score_increasing = True

topic_b = random.choice(data)

while score_increasing:
    topic_a = topic_b
    topic_b = random.choice(data)

    while topic_a == topic_b:
        account_b = random.choice(data)

    name_a = topic_a["name"]
    description_a = topic_a["description"]
    country_a = topic_a["country"]
    follower_count_a = topic_a["follower_count"]

    name_b = topic_b["name"]
    description_b = topic_b["description"]
    country_b = topic_b["country"]
    follower_count_b = topic_b["follower_count"]

    print(f"Compare A: {name_a}, a {description_a}, from {country_a}.")
    print(vs)
    print(f"Against B: {name_b}, a {description_b}, from {country_b}.")

    guess = input("Who has more followers? A/B?: ")

    print("\n" * 100)
    print(logo)

    if follower_count_a > follower_count_b:
        correct_answer = "a"
    else:
        correct_answer = "b"

    if guess == correct_answer:
        score += 1
        print(f"Correct! Current score: {score}")
    else:
        print(f"Wrong, Final score: {score}")
        score_increasing = False
