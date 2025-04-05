## LeetCodeの勉強用リポジトリ

### ✏️ 設定
* [LeetCode - Visual Studio extension](https://marketplace.visualstudio.com/items/?itemName=LeetCode.vscode-leetcode)をインストール
    * ファイル保存先を変更
        ```
        <!-- setting.json -->

        ~~~~~~~~~~~~~~~~~
        "leetcode.filePath": {
        "default": {
            "folder": "work/${language}/${tag}",
            "filename": "${id}_${PascalCaseName}.${ext}"
        }
        ~~~~~~~~~~~~~~~~~
        }
        ```
### 💡 コマンド
* 勉強が終わった時：`make done`