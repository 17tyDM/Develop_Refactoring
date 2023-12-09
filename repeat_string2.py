import numpy

def repeat_string_refactoring(string, num_horizontal, num_vertical):
    """文字列を行と列に繰り返し出力する

    Args:
        string (str): 表示する文字列
        num_horizontal (int): 列方向に文字列表示を繰り返す数
        num_vertical (int): 行方向に文字列表示を繰り返す数
    """
    try:
        # TODO:文字列の長さが5文字以上10文字以下かどうかをチェック
        if not (5 <= len(string) <= 10):
            raise ValueError("文字列は5文字以上10文字以下である必要があります。")

        # TODO:文字列がアルファベット以外の文字を含んでいないかをチェック
        if not string.isalpha():
            raise ValueError("文字列にはアルファベット以外の文字が含まれています。")

        # 文字列の繰り返し
        repeated_vertical = '\n'.join([string * num_horizontal for _ in range(num_vertical)])

        return repeated_vertical
    except ValueError as e:
        return f"エラー: {e}"
    
horizontal = numpy.random.randint(0,10)
vertical = numpy.random.randint(0,10)
print(f"横x{horizontal}")
print(f"縦x{vertical}")
print(repeat_string_refactoring("hello", horizontal, vertical))