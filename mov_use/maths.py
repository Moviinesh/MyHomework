def cal(no1, uni, no2):
    if uni == "+":
        print(int(no1) + int(no2))
    if uni == "-":
        print(int(no1) - int(no2))
    if uni == "*":
        print(int(no1) * int(no2))
    if uni == "/":
        print(int(no1) / int(no2))

def Maths_Timetables(number_of_times):
    times_sheet_data = int(number_of_times) + 1
    times_sheet = int(number_of_times) * 13
    for i in range(int(number_of_times), times_sheet, times_sheet_data - 1):
        print(i)

# Try Functions

