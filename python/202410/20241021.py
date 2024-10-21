# ### お題: 名前リストの入出力
# 1. **入力**: 「names.txt」というファイルを作成して、その中に複数の名前（1行に1つの名前）を書いておく。
# 2. **処理**: そのファイルを読み込んで、名前の一覧を表示し、さらに「names_sorted.txt」というファイルにアルファベット順で名前をソートして保存する。
# 3. **出力**: プログラムを実行した後、「names_sorted.txt」にソートされた名前のリストが出力されていることを確認。

with open('names.txt', 'r', encoding='utf-8') as file:
    names = file.readlines()
    names = [name.strip() for name in names]
    print(names)

with open('names_sorted.txt', 'w', encoding='utf-8') as file:
    for name in sorted(names):
        file.write(name + '\n')

with open('names_sorted.txt', 'r', encoding='utf-8') as file:
    names = file.readlines()
    names = [name.strip() for name in names]
    print(names)