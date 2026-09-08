# program finds how often a streak of six heads or tailes occur
# in a randomly generated list of heads or tails
import random

number_of_streaks = 0
number_of_streaks2 = 0

def generate_result(lenght: int) -> list:
    return ["H" if random.random() < 0.5 else "T" for dummy in range(lenght)]

def count_six_streak(store: list):
    global number_of_streaks
    combined = "".join(store)
    number_of_streaks += (combined.count("HHHHHH") + combined.count("TTTTTT"))

def count_six_streak2(store: list):
    # implemented without the count
    global number_of_streaks2
    streak = 1
    for i in range(1, len(store)):
        if store[i] == store[i - 1]:
            streak += 1
        else:
            streak = 1

        if streak == 6:
            number_of_streaks2 += 1
            streak = 0

exp_str_count = 0
exp_str_count2 = 0

for i in range(10000):
    throws = generate_result(100)
    count_six_streak(throws)
    count_six_streak2(throws)

print(number_of_streaks2, number_of_streaks)
print(f"percentage: {exp_str_count / 10000 * 100}")
print(f"percentage: {exp_str_count2 / 10000 * 100}")

