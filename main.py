import re
import os
from deep_translator import GoogleTranslator

def read_file(path: str) -> str:
    
    res = ""
    with open(path, "r", encoding="utf8") as fp:
        res = res.join(fp.readlines())

    return res

def find_chinese(string: str) -> list[str]:
    return set(re.findall(r'[\u4e00-\u9fff]+', string))


def translate(chinese_words):
    res = []
    for word in chinese_words:
        res.append(GoogleTranslator(source='zh-CN', target='en').translate(word))
    return res

def get_files() -> list[str]:
    directory_path = "./src"
    extension = ".tsx"
    result = []
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith(extension):
                result.append(os.path.join(dirpath, filename))
    return result



if __name__ == "__main__":
    # chinese = find_chinese(read_file("./src/card.tsx"))

    chinese_words = set()

    for each in get_files():
        chinese = find_chinese(read_file(each))
        chinese_words.update(chinese)

    print(list(chinese_words))

    # print(chinese)
    # print(translate(chinese))

