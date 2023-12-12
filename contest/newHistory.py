with open('input.txt', 'r') as file:
    start = list(map(int, file.readline().split()))
    end = list(map(int, file.readline().split()))

days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def countSeconds():
    end_sec = end[3] * 60 * 60 + end[4] * 60 + end[5]
    start_sec = start[3] * 60 * 60 + start[4] * 60 + start[5]
    if end_sec > start_sec:
        return end_sec - start_sec
    else:
        end_sec = 24 * 60 * 60 + end_sec
        end[2] -= 1
        if end[2] == 0:
            end[2] += days_of_month[end[1] - 1]
        return end_sec - start_sec


def countDays():
    if end[2] > start[2]:
        return end[2] - start[2]
    else:
        end[1] -= 1
        if end[1] == 0:
            end[1] = 12
            end[0] -= 1
        return days_of_month[end[1] - 1] + end[2] - start[2]


def countDayFromMonth():
    end_day = sum(days_of_month[:end[1] - 1])
    start_day = sum(days_of_month[:start[1]])
    if end_day > start_day:
        return end_day - start_day
    else:
        end_day += 365
        end[0] -= 1
        return end_day - start_day


def countDayFromYear():
    return (end[0] - start[0]) * 365


sec = countSeconds()
days = countDayFromMonth() + countDayFromYear() + countDays()
with open('output.txt', 'w') as file:
    file.write(f"{days} {sec}\n")
