from collections import defaultdict

def read_puzzlefile(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


def find_winning_numbers(line):
    numbers_str = line.split(":")[1].split("|")
    win_numbers, curr_numbers = numbers_str
    win_numbers = win_numbers.strip()
    curr_numbers = curr_numbers.strip()
    win_numbers = set(map(int, win_numbers.split()))
    curr_numbers = set(map(int, curr_numbers.split()))
    return curr_numbers.intersection(win_numbers)

def find_total_num_scatchcards(line_generator):
    
    card_loops = defaultdict(lambda: 1) #create a hashmap/dictionary that returns the value 1 for any key not present.
    card_number = 1

    for line in line_generator:
        winning_numbers = find_winning_numbers(line) #find which numbers won in the current line.
#            print(card_number, card_loops[card_number])
        for _ in range(card_loops[card_number]): # for the current line's card ID AND any previously rewarded cards of the same ID:
            for j in range(card_number+1, card_number+1+len(winning_numbers)): # reward user with as many subsequent scatchcards as the number of won numbers.
                card_loops[j] = card_loops[j] + 1

        card_number += 1

    #print(dict(card_loops))
    print(f"Total number of scratchcards : {sum(card_loops.values())}")

if __name__ == "__main__":
    generator = read_puzzlefile("input.txt")
    find_total_num_scatchcards(generator)
