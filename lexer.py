


import re
import sys

# Reserved keywords
keywords = {
    "int", "float", "if",
    "else", "while", "return"
}

# Token patterns
token_patterns = [
    ("COMMENT", r"//.*"),
    ("STRING", r'"[^"]*"'),
    ("NUMBER", r'\d+(\.\d+)?'),
    ("OPERATOR", r'==|!=|<=|>=|\+|-|\*|/|=|<|>'),
    ("DELIMITER", r'[\(\)\{\}\[\],;:]'),
    ("IDENTIFIER", r'[A-Za-z_][A-Za-z0-9_]*'),
    ("WHITESPACE", r'\s+'),
]


def lexical_analyzer(code):
    position = 0

    while position < len(code):
        match = None

        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code, position)

            if match:
                lexeme = match.group(0)

                # Ignore whitespace
                if token_type == "WHITESPACE":
                    pass

                # Skip comments
                elif token_type == "COMMENT":
                    pass

                else:
                    # Check if identifier is actually a keyword
                    if token_type == "IDENTIFIER" and lexeme in keywords:
                        token_type = "KEYWORD"

                    print(f"<{token_type}, {lexeme}>")

                position = match.end(0)
                break

        # Handle invalid characters
        if not match:
            print(f"ERROR: Unrecognized character '{code[position]}'")
            position += 1


# Main Program
if len(sys.argv) != 2:
    print("Usage: python lexer.py <input_file>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        source_code = file.read()

    lexical_analyzer(source_code)

except FileNotFoundError:
    print("Error: File not found.")