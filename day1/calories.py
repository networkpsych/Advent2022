
def elf_dict(file):
    snack_calories = []
    calories_list = []
    calorie_totals = {}
    elf = 1

    for line in file:
        if line == '\n':
            elf += 1
            calorie_totals[elf] = sum(snack_calories)
            calories_list.append(sum(snack_calories))
            snack_calories = []
        else:
            snack_calories.append(int(line))
    return calorie_totals, sorted(calories_list)

def max_all_elves(elf_dict):
    return max(elf_dict.values())

def top_three_elves(elf_list):
    # I need to fix this
    return sum(elf_list[-3:])



file = open('./day1/calories.txt')
elf_snacks = file.readlines()
all_elf_calories = elf_dict(elf_snacks)


print(f"Max calories: {max_all_elves(all_elf_calories[0])}\n")
print(f"Top three calories: {top_three_elves(all_elf_calories[1])}")

