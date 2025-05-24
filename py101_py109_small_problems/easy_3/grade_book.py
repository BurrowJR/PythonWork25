def get_grade(score_1, score_2, score_3):
    mean = (score_1 + score_2 + score_3) / 3
    if mean >= 90:
        return'A'
    elif mean >= 80:
        return 'B'
    elif mean >= 70:
        return 'C'
    elif mean >= 60:
        return 'D'
    else:
        return 'F'


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True