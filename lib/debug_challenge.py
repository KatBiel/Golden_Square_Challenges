def get_most_common_letter(text):
    counter = {}
    for char in text:
        if char.isalnum():
            counter[char] = counter.get(char, 0) + 1
        # print(f'counter[char] is {counter[char]} for {char}')
    letter = max(counter.items(), key=lambda item: item[1])[0]
    # print(f'sorted counter is {sorted(counter.items(), key=lambda item: item[1])}')
    # print(f'letter is {letter}')
    # print(f'Counter is {counter}')
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")