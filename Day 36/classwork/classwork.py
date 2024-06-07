#1
def sum_of_two_lowest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]

example = [12, 15, 42, 21, 7]
result = sum_of_two_lowest_numbers(example)
print(result) 
 
 
#2

#3


#4
def calculate_score(correct_answers, student_answers):
    score = 0
    
    for correct, student in (correct_answers, student_answers):
        if student == "":
            score += 0
        elif student == correct:
            score += 4
        else:
            score -= 1
    
    return max(score, 0)

correct_answers = ["a", "a", "c", "b"]
student_answers = ["a", "c", "b", "d"]
print(calculate_score(correct_answers, student_answers))
#5
def rowWeights(weights):
    team1_sum = 0
    team2_sum = 0

    for i in range(len(weights)):
        if i % 2 == 0:
            team1_sum += weights[i]
        else:
            team2_sum += weights[i]
    
    return (team1_sum, team2_sum)

print(rowWeights([50, 60, 70, 80])) 