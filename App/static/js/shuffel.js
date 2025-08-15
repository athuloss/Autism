const puzzleContainer = document.getElementById('puzzle-container');
const correctSound = document.getElementById('correct-sound');

// The image to be used for the puzzle
const imageUrl = 'path/to/your-image.jpg'; 

const rows = 3;  // Number of rows in the puzzle
const cols = 3;  // Number of columns in the puzzle

let pieces = []; // To store puzzle pieces

// Create puzzle pieces
function createPuzzle() {
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const piece = document.createElement('div');
      piece.classList.add('puzzle-piece');
      piece.setAttribute('draggable', true);

      // Set the background image position for each piece to crop the image
      piece.style.backgroundImage = `url(${imageUrl})`;
      piece.style.backgroundPosition = `-${col * 100}px -${row * 100}px`; // This crops the image

      // Set the correct position for the piece (you can store it in the dataset for later comparison)
      piece.dataset.position = `${row},${col}`;

      pieces.push(piece);
      puzzleContainer.appendChild(piece);

      piece.addEventListener('dragstart', dragStart);
      piece.addEventListener('dragover', allowDrop);
      piece.addEventListener('drop', drop);
    }
  }

  // Shuffle pieces
  shufflePuzzle();
}

// Shuffle the puzzle pieces
function shufflePuzzle() {
  const shuffledPieces = [...pieces];
  shuffledPieces.sort(() => Math.random() - 0.5);
  
  puzzleContainer.innerHTML = '';
  shuffledPieces.forEach(piece => {
    puzzleContainer.appendChild(piece);
  });
}

// Handle the dragstart event
function dragStart(event) {
  event.dataTransfer.setData('text', event.target.dataset.position);
}

// Allow drop on the puzzle pieces
function allowDrop(event) {
  event.preventDefault();
}

// Handle the drop event
function drop(event) {
  event.preventDefault();

  const draggedPosition = event.dataTransfer.getData('text');
  const droppedPosition = event.target.dataset.position;

  // Swap positions if valid
  if (draggedPosition !== droppedPosition) {
    const draggedPiece = document.querySelector(`[data-position="${draggedPosition}"]`);
    const droppedPiece = document.querySelector(`[data-position="${droppedPosition}"]`);

    const tempPosition = draggedPiece.dataset.position;
    draggedPiece.dataset.position = droppedPiece.dataset.position;
    droppedPiece.dataset.position = tempPosition;

    // Check if the puzzle is solved
    checkPuzzle();
  }
}

// Check if the puzzle is solved
function checkPuzzle() {
  const allCorrect = pieces.every(piece => {
    const position = piece.dataset.position.split(',');
    const row = parseInt(position[0]);
    const col = parseInt(position[1]);

    return piece.dataset.position === `${row},${col}`;
  });

  if (allCorrect) {
    alert('Puzzle solved!');
    correctSound.play();
  }
}

// Initialize the puzzle
createPuzzle();
