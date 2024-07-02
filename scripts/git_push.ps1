# PowerShellスクリプトのファイル名を git_push.ps1 として保存する
# コミットメッセージをスクリプトの引数として渡す
#
# 使い方：
# .\git_push.ps1 "コミットメッセージ"


# リポジトリのルートディレクトリに移動する
cd (git rev-parse --show-toplevel)

# 変更をステージング
git add .

# コミットメッセージを引数から取得してコミット
git commit -m $args[0]

# 変更をリモートリポジトリにプッシュ
git push origin main
