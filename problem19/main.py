def isLeapYear(year: int) -> bool:
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0

def main():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    current_day = 1
    sunday_count = 0

    for year in range(1900, 2001):
        for month in months:
            if isLeapYear(year):
                months[1] = 29
            else:
                months[1] = 28
            if current_day == 0 and year > 1900:
                sunday_count += 1

            current_day = (current_day + month) % 7
    print(sunday_count)


if __name__ == "__main__":
    main()