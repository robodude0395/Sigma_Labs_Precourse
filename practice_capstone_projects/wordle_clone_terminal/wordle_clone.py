import random
from rich.console import Console
from rich.theme import Theme
from string import ascii_letters, ascii_uppercase

def get_random_word_from_file(filepath):
    """Return a random word from a word list file, skipping comment lines."""
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # skip empty lines & comments
                continue
            words.append(line)

    if not words:
        raise ValueError("No valid words found in file!")

    return random.choice(words)

def show_guesses(guesses, correct_word):
    global console
    letter_status = {letter: letter for letter in ascii_uppercase}
    
    for guess in guesses:
        styled_guess = []
        for letter, correct, in zip(guess, correct_word):
            if letter == correct:
                style = "bold white on green"
            elif letter in correct_word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"

        console.print("".join(styled_guess), justify="center")
    console.print("\n" + "".join(letter_status.values()), justify="center")

def  game_over(guesses, correct_word, guessed_correctly):
    global console
    refresh_page(headline="Game Over")
    show_guesses(guesses, correct_word)
    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {correct_word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {correct_word}[/]")

def get_all_valid_words(filepath):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # skip empty lines & comments
                continue
            words.append(line)

    if not words:
        raise ValueError("No valid words found in file!")
    return words

def guess_word(previous_guesses):
    global console
    global valid_words

    guess = console.input("\nGuess word: ").upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses)
    
    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f"Invalid letter: '{invalid}'. Please use English letters.",
            style="warning",
        )
        return guess_word(previous_guesses)

    if len(guess) != 5:
        console.print(f"'Your guess must be 5 letters.", style="warning")
        return guess_word(previous_guesses)

    if guess not in valid_words:
        console.print(f"'{guess}' is not a valid word.", style="warning")
        return guess_word(previous_guesses)

    return guess

def refresh_page(headline):
    global console
    console.clear()
    console.rule(f"[bold blue]:zap: {headline} :zap:[/]\n", style="warning")

words_list_path = "valid-wordle-words.txt"
console = Console(width=40, theme=Theme({"warning": "red on yellow"}))
valid_words = get_all_valid_words(words_list_path)

NUM_LETTERS = 5
NUM_GUESSES = 6
guesses = ["_"*NUM_LETTERS] * NUM_GUESSES

#-----MAIN PROGRAM-----
def main():
    global guesses
    global words_list_path

    correct_word = get_random_word_from_file(words_list_path)

    guessed_correctly = False

    for idx in range(6): #Six tries
        refresh_page(f"Guess {idx + 1}")
        show_guesses(guesses, correct_word)
        guess = guess_word(guesses)
        guesses[idx] = guess

        if guesses[idx] == correct_word:
            print("CORRECT")
            guessed_correctly = True
            break

    game_over(guesses, correct_word, guessed_correctly)

if __name__ == "__main__":
    main()