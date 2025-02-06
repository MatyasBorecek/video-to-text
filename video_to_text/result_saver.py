import codecs


def save_result_to_file(text: str, file_path: str = "result.txt") -> None:
    with codecs.open(file_path, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"[INFO] Results saved successfully to {file_path}.")
