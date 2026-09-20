def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the path and try again.")
        return 0
    except OSError as exc:
        print(f"An unexpected file error occurred: {exc}")
        return 0

    words = content.split()
    word_count = len(words)
    print(f"File '{file_path}' opened successfully.")
    print(f"Total word count: {word_count}")
    return word_count


if __name__ == "__main__":
    file_name = input("Enter the path/name of the text file to count words: ").strip()
    if file_name:
        count_words(file_name)
    else:
        print("Please provide a file path.")