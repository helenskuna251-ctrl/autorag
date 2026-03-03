import os


# 支持的文本类型
TEXT_EXTENSIONS = {".txt", ".md"}


def parse_file(file_path: str) -> str:
    """
    根据文件类型解析文件内容
    返回纯文本字符串
    """

    # 获取文件扩展名
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()  # 防止 .TXT 这种情况

    if ext in TEXT_EXTENSIONS:
        return parse_text(file_path)

    elif ext == ".pdf":
        return parse_pdf(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")


def parse_text(file_path: str) -> str:
    """
    解析纯文本文件（txt / md）
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def parse_pdf(file_path: str) -> str:
    """
    解析 PDF 文件（暂未实现）
    """
    return "PDF parsing not implemented yet"