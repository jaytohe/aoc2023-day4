def read_puzzlefile(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

def find_sum_winning_numbers(line_generator):
    total_points_of_cards = 0
    for line in generator:
        all_numbers_str = line.split(":")[1].split("|") # split on the | seperator
        win_numbers, curr_numbers = all_numbers_str # unpack to winning numbers and current numbers
        win_numbers = win_numbers.strip() #remove head and tail whitespaces.
        curr_numbers = curr_numbers.strip()
        win_numbers = set(map(int, win_numbers.split())) #split on spaces and map each string number to integer and create a set.
        curr_numbers = set(map(int, curr_numbers.split()))


        #print(win_numbers, end="\t")
        #print(curr_numbers)

        found_win_numbers = curr_numbers.intersection(win_numbers) #Find which winning numbers are contained in the current numbers.

        card_points = 0
        if len(found_win_numbers) > 0:
            card_points = 2 ** (len(found_win_numbers) -1) #calculate card points by 2^(n-1)

        total_points_of_cards += card_points

    print(f"The cards are worth {total_points_of_cards} points in total!")

if __name__ == "__main__":
    generator = read_puzzlefile("input.txt")
    find_sum_winning_numbers(generator)
