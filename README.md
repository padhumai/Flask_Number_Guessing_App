<<<<<<< HEAD
# Number Guessing Game

## Project Description
This is a web-based Number Guessing Game developed using Python Flask and MySQL. The user enters their name, selects a difficulty level, and tries to guess a randomly generated number within five attempts. The game provides hints such as "Too High" or "Too Low". The result of every game is stored in a MySQL database.

## Features
- Player name input
- Three difficulty levels (Easy, Medium, Hard)
- Random number generation
- Maximum 5 attempts
- Score calculation
- Too High / Too Low hints
- Win/Lose message
- Game results stored in MySQL database
- Play Again option

## Technologies Used
- Python
- Flask
- HTML
- CSS
- MySQL
- MySQL Connector
- MySQL Workbench
- PyCharm

## Database
Database Name: `number_guessing_game`

Table Name: `game_results`

Columns:
- id
- player_name
- difficulty
- attempts
- score
- result
- played_at

## How to Run
1. Clone the project.
2. Install the required packages.
3. Create the MySQL database and table.
4. Update the MySQL username and password in `app.py`.
5. Run the application:
   ```
   python app.py
   ```
6. Open:
   ```
   http://127.0.0.1:5000
   ```

## Future Improvements
- User Login
- Leaderboard
- Timer
- Better UI
- Game History

## Author
S. Padhumaimathi
=======
# Flask_Number_Guessing_App
A Number Guessing Game Developed Using Python Flask and MySQL
>>>>>>> c0045b05c4d63058c069249e1b6a5b1ecfb45d97
