

def calcTotQuestions(k:int, n:int) -> int:
    tot_time = 240
    rem_time = tot_time - k

    tot_questions = 0

    for i in range(1, n+1):
        round_time = 5 * i
        if rem_time < round_time:
            break

        tot_questions +=1
        rem_time -=round_time

    return tot_questions


data = input()
data = data.split()
n = int(data[0])
k = int(data[1])

print(calcTotQuestions(k ,n))