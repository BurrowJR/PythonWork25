# ![](./flowchart.drawio.svg)

def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number

        iterator += 1

    return saved_number

print(find_greatest([19, 200, 24, 119, 0, 55]))   # 200