# program generates a random quiz questions and stores them in files
# creates 35 quiz questions
# creates a 50 mcq question files 
# Provides the correct answer and 3 random answers
# randomises the same questions
# writes answers to the 35 files 

import os
from pathlib import Path
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':
    'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
    'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
    'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'west':'Charleston', 
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

def write_to_file(text: str, file: Path) -> None:
    with file.open("a",encoding="UTF-8") as f:
        f.write(text)


def create_quiz_files(num: int) -> None:
    start_text = "Name:\nSchool:\nDate:\n\n\t\t\tQUIZ\n\n"
    
    for i in range(1, num + 1):
        quiz_path = Path.cwd() / "quiz" / f"quiz{i}.txt"
        answer_path = Path.cwd() / "answers" / f"answer{i}.txt"
        Path(quiz_path).touch(exist_ok=False)
        Path(answer_path).touch(exist_ok=False)
        write_to_file(start_text, quiz_path)


def get_answers(capitals: dict, state: str) -> tuple[str, str]:
    answers = list(capitals.values())
    correct_answer = capitals[state]
    correct_index = answers.index(correct_answer)
    chosen = []
    for i in range(4):
        if answers[correct_index] in chosen:
            random.shuffle(answers)
        chosen.append(answers[correct_index])  # this ensures no dublicate answers 
        random.shuffle(answers)
    random.shuffle(chosen)

    answer_str = ""
    for i in range(4):
        answer_str += f"    {"ABCD"[i]}. {chosen[i]}\n"
    correct_letter = "ABCD"[chosen.index(correct_answer)]

    return answer_str, correct_letter

def generate_quiz(quiz_num: int ,states: list, capitals: dict, quiz_path: Path, answer_path: Path):
    for num in range(1, quiz_num + 1):
        ans_str, correct_ans = get_answers(capitals, states[num - 1])
        question = f"{num}. What is the capital of {states[num - 1]}?\n"
        write_to_file(question, quiz_path)
        write_to_file(ans_str, quiz_path)
        write_to_file(f"{num}. {correct_ans}\n", answer_path)


quiz_path = Path.cwd() / "quiz"
answer_path = Path.cwd() / "answers"
quiz_path.mkdir()
answer_path.mkdir() 

for i in range(1, 36):
    quiz_path = Path.cwd() / "quiz" / f"quiz{i}.txt"
    answer_path = Path.cwd() / "answers" / f"answer{i}.txt"
    generate_quiz(50, list(capitals.keys()), capitals, quiz_path, answer_path)
    print(f"created file {i}")
