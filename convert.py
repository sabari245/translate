import os
import re
import csv

translations = {}

with open("dictionary.csv", "r", encoding="utf8") as f:
    reader_obj = csv.reader(f)
    for row in reader_obj:
        if len(row) != 0:
            translations[row[0]] = row[1]

def get_files() -> list[str]:
    directory_path = ".\src"
    extensions = [".tsx", ".ts", ".jsx", ".js", ".md", ".mdx", ".sh"]
    result = []
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            for extension in extensions:
                if filename.endswith(extension):
                    result.append(os.path.join(dirpath, filename))
    return result

def read_file(path: str) -> str:
    res = ""
    with open(path, "r", encoding="utf8") as fp:
        res = res.join(fp.readlines())

    return res

def write_file(path: str, content: str) -> None:
    with open(path, 'w', encoding="utf8") as fp:
        fp.write(content)


def find_chinese(string: str) -> list[str]:
    return set(re.findall(r"[\u4e00-\u9fff]+", string))

if __name__ == "__main__":
    for file in get_files():
        content = read_file(file)

        words = list(find_chinese(content))

        words.sort(key=lambda x: len(x), reverse=True)

        for word in words:
            content = content.replace(word, translations[word])

        # if len(find_chinese(content)) > 0:
        #     # print(content)
        #     print(file, " = ", find_chinese(content))

        write_file(file.replace(r".\src\amis", r".\src\res"), content)

