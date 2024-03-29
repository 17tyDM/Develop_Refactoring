'''
以下の機能をもつプログラムを作成する
・コマンドラインで7つの引数を指定する
・最初の引数が月曜日のタスク、最後の引数が日曜日のタスクとして以下の形式で出力する
    月曜日：（１つ目の引数）
    火曜日：（２つ目の引数）
    ～
    日曜日：（７つ目の引数）
・但し、上記の出力は月曜日に実行した際の出力順序で
    プログラムが実行された曜日を先頭にしてタスクを出力する
    例）土曜日に実行された場合
    土曜日：（６つ目の引数）
    日曜日：（７つ目の引数）
    月曜日：（１つ目の引数）
    ～
    金曜日：（５つ目の引数）
・引数が７つ以外であれば利用法を表示する

'''
from sys import argv
from datetime import datetime

def main(arg):
    """一週間の各曜日に対するタスク
    Args:
        arg (List<String>): タスク用配列
    """
    # 実行日の曜日に対応したインデックスを取得
    today_index = datetime.now().weekday()
    # 曜日の配列
    week_list = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    # コマンドライン引数から渡されたタスクを入れる変数
    tasks = []
    # コマンドライン引数から渡された値をtasks変数に入れる処理
    for task in arg:
        tasks.append(task)
    # 実行日の曜日を先頭にし出力する処理
    for i in range(7):
        # 実行日の曜日を先頭にしインデックス番号として扱えるようにする処理
        day_index = (today_index + i) % 7
        # 出力処理
        print(f"{week_list[day_index]}:{tasks[day_index]}")

if __name__ == '__main__':
    # コマンドライン引数(タスク数)が7つではなかった時
    if len(argv) != 8:
        print('曜日毎のタスクを７つ入力してください')
        exit(0) # 正常終了

    main(argv[1:]) # コマンドライン引数[1]~を文字列型配列としてmain関数の引数にセット