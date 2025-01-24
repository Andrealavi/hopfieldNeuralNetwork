# Hopfield Network Pattern Recognition

A Python implementation of a Hopfield Neural Network with a graphical user interface for pattern recognition and storage. This project demonstrates the capabilities of Hopfield networks in recognizing and reconstructing patterns, making it useful for educational purposes and pattern recognition experiments.

## Features

- **Interactive GUI**: User-friendly interface for drawing and testing patterns
- **Pattern Recognition**: Ability to recognize and reconstruct learned patterns
- **Pattern Storage**: Functionality to add new patterns to the network
- **Visual Feedback**: Real-time visualization of recognition results
- **Pattern Management**: Clear and reset functionality for the input grid
- **Pre-trained Patterns**: Comes with sample patterns for immediate testing

## Prerequisites

- Python 3.x
- Tkinter (usually comes with Python installation)
- typing module

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hopfield-network-recognition.git
cd hopfield-network-recognition
```

2. Ensure you have all prerequisites installed:
```bash
python -m tkinter # To verify Tkinter installation
```

## Usage

1. Run the main application:
```bash
python main.py
```

2. Using the application:
   - Left-click on the grid cells to draw a pattern (cells toggle between white and blue)
   - Click "Input" to test if the pattern matches any stored patterns
   - Click "Clear" to reset the input grid
   - Click "Add Pattern" to store a new pattern in the network

3. Pattern files:
   - The application loads initial patterns from the `patterns` directory
   - Pattern files should be formatted as space-separated values with 1 (active) and -1 (inactive)
   - Default patterns are numbered (1.txt, 2.txt, 3.txt)

## Project Structure

- `main.py`: Contains the GUI implementation and application entry point
- `HopfieldNetwork.py`: Core implementation of the Hopfield Neural Network
- `patterns/`: Directory containing training patterns

## Technical Details

The Hopfield Network implementation includes:
- Weight matrix calculation for pattern storage
- Pattern classification using energy minimization
- Support for multiple pattern storage and recognition
- Configurable network size (default: 9x9 neurons)
