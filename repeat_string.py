import sys

def repeat_string(string, num_horizontal, num_vertical):
    try:
        # 文字列の長さが5文字以上10文字以下かどうかをチェック
        if not (5 <= len(string) <= 10):
            raise ValueError("文字列は5文字以上10文字以下である必要があります。")

        # 文字列がアルファベット以外の文字を含んでいないかをチェック
        if not string.isalpha():
            raise ValueError("文字列にはアルファベット以外の文字が含まれています。")

        # 文字列の繰り返し
        repeated_vertical = '\n'.join([string * num_horizontal for _ in range(num_vertical)])

        return repeated_vertical
    except ValueError as e:
        return f"エラー: {e}"
