import os
import re


def read_file(path: str) -> str:
    res = ""
    with open(path, "r", encoding="utf8") as fp:
        res = res.join(fp.readlines())

    return res


def find_chinese(string: str) -> list[str]:
    return set(re.findall(r"[\u4e00-\u9fff]+", string))


def get_files(directory_path: str = "./src", extensions: list[str] = []) -> list[str]:
    extensions_final = [".tsx", ".ts", ".jsx", ".js", ".md", ".mdx", ".sh"] + extensions
    result = []
    for dirpath, _, filenames in os.walk(directory_path):
        for filename in filenames:
            for extension in extensions_final:
                if filename.endswith(extension):
                    result.append(os.path.join(dirpath, filename))
    return result


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf8") as fp:
        fp.write(content)
