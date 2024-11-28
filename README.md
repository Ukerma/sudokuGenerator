<h1>🧩 Sudoku Puzzle Generator</h1>
<p>
   This project is a <strong>Sudoku Puzzle Generator</strong> created in Python. It allows users to generate Sudoku puzzles at different difficulty levels (Easy, Medium, Hard) and save the puzzle to a file. The program implements Sudoku rules to ensure the generated puzzle is solvable and unique.
</p>

<h2>🛠️ Features</h2>
<ul>
   <li> <strong>Difficulty Levels:</strong> Users can choose from Easy, Medium, and Hard difficulty levels.</li>
   <li> <strong>Random Puzzle Generation:</strong> Creates a valid Sudoku puzzle based on the chosen difficulty level.</li>
   <li> <strong>Display Sudoku Board:</strong> Prints the Sudoku puzzle in a user-friendly grid format.</li>
   <li> <strong>Save to File:</strong> Allows users to save the generated puzzle to a text file (e.g., <code>kolay.txt</code>, <code>orta.txt</code>, <code>zor.txt</code>).</li>
   <li> <strong>Input Validation:</strong> Ensures valid input for selecting difficulty and saving the puzzle.</li>
</ul>

<h2>⚙️ Technologies Used</h2>
<ul>
   <li> <strong>Language:</strong> Python</li>
   <li> <strong>Libraries:</strong> 
      <ul>
         <li><code>random</code>: Used for generating random numbers and shuffling.</li>
      </ul>
   </li>
</ul>

<h2>🚀 How to Use</h2>
<ol>
   <li> Run the script using a Python IDE or terminal.</li>
   <li> Choose a difficulty level from the menu:</li>
   <ul>
      <li><strong>1:</strong> Easy</li>
      <li><strong>2:</strong> Medium</li>
      <li><strong>3:</strong> Hard</li>
   </ul>
   <li> View the generated Sudoku puzzle on the console.</li>
   <li> Choose whether to save the puzzle:</li>
   <ul>
      <li>Type <strong>Evet</strong> to save the puzzle to a text file.</li>
      <li>Type <strong>Hayır</strong> to skip saving and exit the program.</li>
   </ul>
   <li> If saved, the puzzle will be written to a file named based on the difficulty level (e.g., <code>kolay.txt</code> for Easy).</li>
</ol>

<h2>💡 Example Output</h2>
<pre>
╔══╣ SUDOKU SEVIYELERI ╠══╗
║    » 1· Kolay           ║
║    » 2· Orta            ║
║    » 3· Zor             ║
╚═════════════════════════╝

════════════╦═════════════╦════════════
  5  0  0   ║   0  9  3   ║  0  0  8  
  6  7  3   ║   0  0  0   ║  9  5  0  
  0  0  0   ║   6  8  0   ║  7  0  4  
════════════╬═════════════╬════════════
  3  8  9   ║   0  0  4   ║  6  0  7  
  7  6  4   ║   0  2  0   ║  0  8  0  
  0  5  0   ║   0  3  0   ║  0  0  0  
════════════╬═════════════╬════════════
  9  0  7   ║   0  4  5   ║  0  0  2  
  0  0  0   ║   0  0  2   ║  0  0  0  
  4  0  2   ║   9  0  7   ║  0  0  0  
════════════╩═════════════╩════════════

» Sudoku şablonu kolay.txt dosyasına kaydedildi.
</pre>

<h2>👨‍💻 Author</h2>
<p>
   This project was developed by <strong>Umut Kerim ACAR (ukerma)</strong> and <strong>Tuna DURUKAN (Ranewen)</strong>.
</p>
