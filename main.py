import os
import sys


class SpeckError(Exception):
    pass


def interpret(code):
    value = 0
    started = False
    output = []

    alphabet_mode = False
    combined_mode = False

    i = 0
    n = len(code)
    while i < n:
        pos = i + 1
        command = code[i]

        if command.isspace():
            i += 1
            continue

        if command == ',':
            if started:
                print("Warning: Speck already started. Resetting value.")

            value = 0
            started = True
            alphabet_mode = False
            combined_mode = False
            i += 1

        elif command == '+':
            if not started:
                raise SpeckError(
                    f"Error at position {pos}: Program not started."
                )

            value += 1
            i += 1

        elif command == '-':
            if not started:
                raise SpeckError(
                    f"Error at position {pos}: Program not started."
                )

            value -= 1
            i += 1

        elif command == ':':
            if not started:
                raise SpeckError(
                    f"Error at position {pos}: Program not started."
                )

            alphabet_mode = True
            i += 1

        elif command == ';':
            if not started:
                raise SpeckError(
                    f"Error at position {pos}: Program not started."
                )

            combined_mode = True
            i += 1

        elif command == '_':
            if not started:
                raise SpeckError(
                    f"Error at position {pos}: Program not started."
                )

            # Check if next command is also '_' (forming '__' for space)
            next_i = i + 1
            while next_i < n and code[next_i].isspace():
                next_i += 1

            if next_i < n and code[next_i] == '_':
                output.append(" ")
                value = 0
                i = next_i + 1
            else:
                value = 0
                i += 1

        elif command == '.':
            if not started:
                raise SpeckError(
                    f"Error at position {pos}: Program not started."
                )

            if combined_mode:
                alphabet = chr((value % 26) + ord('A'))
                output.append(alphabet + str(value))

            elif alphabet_mode:
                alphabet = chr((value % 26) + ord('A'))
                output.append(alphabet)

            else:
                output.append(str(value))
            i += 1

        else:
            raise SpeckError(
                f"Error at position {pos}: Unknown command '{command}'."
            )

    if not started:
        print("Warning: Program has no start command ','.")

    return "".join(output)


VALID_EXTENSIONS = (".speck", ".spk")


def resolve_file(filepath):
    """
    Resolves the given filepath checking for .speck and .spk extensions.
    Returns (resolved_path, error_message).
    """
    if os.path.isfile(filepath):
        if not filepath.lower().endswith(VALID_EXTENSIONS):
            return None, f"Error: Invalid file extension for '{filepath}'. Only .speck and .spk are supported."
        return filepath, None

    # Try appending valid extensions if not already provided
    for ext in VALID_EXTENSIONS:
        candidate = filepath + ext
        if os.path.isfile(candidate):
            return candidate, None

    if filepath.lower().endswith(VALID_EXTENSIONS):
        return None, f"Error: File '{filepath}' not found."

    return None, f"Error: File '{filepath}' not found (.speck or .spk)."


def run_file(filepath):
    """
    Reads and executes a Speck source file.
    Returns True if executed successfully, False otherwise.
    """
    target_path, err = resolve_file(filepath)
    if err:
        print(err)
        return False

    try:
        with open(target_path, "r", encoding="utf-8") as f:
            code = f.read()
    except OSError as e:
        print(f"Error reading file '{target_path}': {e}")
        return False

    try:
        result = interpret(code)
        if result:
            print(result)
        return True
    except SpeckError as error:
        print(error)
        return False


def repl():
    """
    Interactive Read-Eval-Print Loop for Speck.
    """
    print("Speck Programming Language")
    print("Type 'exit' to quit, or 'run <file>' to execute a file.")
    print()

    while True:
        try:
            code = input("speck> ").strip()

            if not code:
                continue

            if code.lower() == "exit":
                break

            if code.lower().startswith("run ") or code.lower().startswith("load "):
                file_arg = code.split(maxsplit=1)[1].strip().strip('\'"')
                run_file(file_arg)
                continue

            result = interpret(code)

            if result:
                print(result)

        except SpeckError as error:
            print(error)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting Speck.")
            break


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("Usage: python main.py [file.spk | file.speck]")
            return

        success = run_file(sys.argv[1])
        if not success:
            sys.exit(1)
    else:
        repl()


if __name__ == "__main__":
    main()

    