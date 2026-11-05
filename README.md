# Speck

A minimalist, accumulator-based esoteric programming language and interpreter written in Python.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.x](https://img.shields.io/badge/Python-3.x-green.svg)

---

## Overview

**Speck** is an ultra-minimalist language that manipulates an internal accumulator value using single-character commands. It supports numeric output, alphabet mapping (A–Z), combined alphanumeric output, and character chaining.

The interpreter supports:
- **Interactive REPL** mode.
- **File execution** from the CLI and inside the REPL.
- Dual file extensions: `.speck` and shortened `.spk`.

---

## Table of Contents

- [Commands Reference](#commands-reference)
- [Output Modes](#output-modes)
- [Installation & Requirements](#installation--requirements)
- [Usage](#usage)
  - [Interactive REPL](#interactive-repl)
  - [Running Files from the Command Line](#running-files-from-the-command-line)
  - [Running Files from the REPL](#running-files-from-the-repl)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [License](#license)

---

## Commands Reference

All non-whitespace characters in Speck represent instructions. Whitespaces and newlines are ignored.

| Command | Name | Description |
| :---: | :--- | :--- |
| `,` | **Start / Reset** | Starts the program and resets `value = 0` and all modes. Emits a warning if called when already started. |
| `+` | **Increment** | Increases the accumulator `value` by 1. |
| `-` | **Decrement** | Decreases the accumulator `value` by 1. |
| `:` | **Alphabet Mode** | Enables uppercase alphabet output mode (maps value modulo 26 to `A`–`Z`). |
| `;` | **Combined Mode** | Enables combined mode (outputs letter + numeric value, e.g. `D3`). |
| `_` | **Character Reset** | Resets `value = 0` without warning, keeping current modes active. Allows chaining multiple characters. |
| `__` | **Word Space** | Appends a space (`' '`) to output and resets `value = 0`. Allows separating multiple words. |
| `.` | **Output** | Outputs the accumulator based on the currently active mode. |

> **Note:** Any command other than `,` before the program has started will raise an `Error: Program not started`.

---

## Output Modes

When the output command (`.`) is executed, the behavior depends on the active mode:

1. **Numeric Mode (Default)**:
   - Prints the raw integer `value` (e.g. `3`).
2. **Alphabet Mode (`:`)**:
   - Computes `(value % 26) + ord('A')` and outputs the resulting uppercase letter:
     - `0` → `A`
     - `1` → `B`
     - `2` → `C`
     - ...
     - `25` → `Z`
3. **Combined Mode (`;`)**:
   - Prints both the alphabet letter and the integer value (e.g. `D3`).

---

## Installation & Requirements

- Python 3.7+
- No external dependencies (uses standard library only).

Clone or copy the project:

```bash
git clone https://github.com/Kaw360/Speck.git
cd Speck
```

---

## Usage

### Interactive REPL

Start the interactive shell:

```bash
python main.py
```

Output:
```text
Speck Programming Language
Type 'exit' to quit, or 'run <file>' to execute a file.

speck> ,+++.
3
speck> exit
```

### Running Files from the Command Line

Speck scripts can use the full extension `.speck` or the shortened extension `.spk`:

```bash
# Run using .spk extension
python main.py samples/number.spk

# Run using .speck extension (or .spk)
python main.py samples/word.spk

# Extension auto-resolution (checks for .spk then .speck)
python main.py samples/number
```

### Running Files from the REPL

You can also run files directly from the interactive REPL without quitting:

```text
speck> run samples/number.spk
3
speck> load samples/word.spk
HI
```

---

## Examples

### 1. Print a Number (`3`)
```text
,+++.
```
- `,` starts the program (`value = 0`).
- `+++` increments value by 3.
- `.` outputs `3`.

### 2. Print a Letter (`B`)
```text
,:+:.
```
- `,` starts the program (`value = 0`).
- `:` activates alphabet mode.
- `+` increments value to `1`.
- `.` outputs `B` (`0 = A, 1 = B`).

### 3. Print Multiple Letters (`HI`)
Using `_` as a delimiter to reset the counter between letters:
```text
,:+++++++._++++++++.
```
- `,` starts the program.
- `:` activates alphabet mode.
- `+++++++.` sets value to `7` and outputs `H`.
- `_` resets value to `0` while maintaining alphabet mode.
- `++++++++.` sets value to `8` and outputs `I`.
- **Output:** `HI`

### 4. Print Multiple Words (`HI HI`)
Using `__` as a word separator (appends a space and resets accumulator):
```text
,:+++++++._++++++++.__+++++++._++++++++.
```
- Outputs `HI`
- `__` appends a space (`" "`) and resets accumulator to `0`.
- Outputs `HI`
- **Output:** `HI HI`

### 5. Combined Mode (`D3`)
```text
,;+++.
```
- `,` starts program.
- `;` activates combined mode.
- `+++` sets value to `3`.
- `.` outputs letter `D` (`3 % 26`) followed by `3` → `D3`.

---

## Project Structure

```text
Speck/
├── LICENSE             # MIT License
├── README.md           # Project documentation
├── main.py             # Interpreter, CLI runner, and REPL
└── samples/            # Example Speck scripts
    ├── combined.spk    # Prints combined letter and number ('D3')
    ├── letter.spk      # Prints a single letter ('D')
    ├── multi.spk       # Prints multiple words ('HI HI')
    ├── number.spk      # Prints a number ('3')
    └── word.spk        # Prints a single word ('HI')
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
