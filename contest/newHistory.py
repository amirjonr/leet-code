with open('input.txt', 'r') as file:
    start = list(map(int, file.readline().split()))
    end = list(map(int, file.readline().split()))

days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year_in_sec = end[0] * 365 * 24 * 60 * 60
month_in_sec = sum(days_of_month[:end[1] - 1]) * 24 * 60 * 60
day_in_sec = end[2] * 24 * 60 * 60
hour_in_sec = end[3] * 60 * 60
min_in_sec = end[4] * 60
sec_end = year_in_sec + month_in_sec + day_in_sec + hour_in_sec + min_in_sec + end[5]

year_in_sec = start[0] * 365 * 24 * 60 * 60
month_in_sec = sum(days_of_month[:start[1] - 1]) * 24 * 60 * 60
day_in_sec = start[2] * 24 * 60 * 60
hour_in_sec = start[3] * 60 * 60
min_in_sec = start[4] * 60
sec_start = year_in_sec + month_in_sec + day_in_sec + hour_in_sec + min_in_sec + start[5]


diff = sec_end - sec_start
days = diff // (24 * 60 * 60)
sec = diff % (24 * 60 * 60)

with open('output.txt', 'w') as file:
    file.write(f"{days} {sec}\n")
