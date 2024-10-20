# WordzGamez

Welcome to **WordzGamez**, a fun and engaging word-guessing game written in Python! Test your vocabulary and word recognition skills as you try to guess the randomly selected word from a hidden word bank. 

## Features

- **Random Word Selection**: The game randomly selects a word from a pre-defined list stored in a text file, ensuring a unique experience each time you play.
- **User Input Validation**: Players can only enter words that match the length of the secret word, helping to maintain the game's challenge.
- **Feedback Mechanism**: After each guess, the game provides immediate feedback:
  - Correct letters are displayed in their correct positions.
  - Misplaced letters (correct letters in the wrong position) are tracked and shown separately.
  - Incorrect letters are also tracked to help refine guesses.
- **Turn Limit**: Players have a maximum of 5 turns to guess the word, adding an exciting time constraint to the gameplay.
- **User-Friendly Interface**: The game runs in the terminal, making it accessible and easy to play anywhere.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wordzgamez.git
   ```
2. Navigate to the project directory:
   ```bash
   cd wordzgamez
   ```
3. Ensure you have a `words.txt` file in the same directory, containing the list of words you want to use for the game.
4. Run the game:
   ```bash
   python wordzgamez.py
   ```

## Gameplay Instructions

- When prompted, enter your guess.
- If your guess is valid (matching the length of the secret word), the game will provide feedback.
- Keep track of your misplaced and incorrect letters to improve your next guess.
- Try to guess the word within the allotted turns to win!

## Contributing

Feel free to fork the repository, make improvements, or add features. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Have fun playing **WordzGamez** and challenge your friends to see who can guess the word the fastest! Enjoy the game and happy guessing!
