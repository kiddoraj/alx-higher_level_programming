#!/usr/bin/python3
def text_indentation(text):
    """Prints 2 new lines after ".?:" characters in the input text.

    Args:
        text (str): Input string.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    processed_lines = []

    current_line = ""
    for char in text:
        current_line += char
        if char in punctuation_marks:
            processed_lines.append(current_line.strip())
            current_line = ""

    if current_line:
        processed_lines.append(current_line.strip())

    processed_text = "\n\n".join(processed_lines)
    print(processed_text, end="")
