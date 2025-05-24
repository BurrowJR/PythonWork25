def century(year):
    century = (year // 100)
    if year % 100 != 0:
        century += 1
    suffix = get_suffix(century)
    return f"{century}{suffix}"

def get_suffix(number):
    if 10 <= number % 100 <= 20:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")

print(century(2000))
print(century(5))
print(century(1052))
print(century(11201))
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True