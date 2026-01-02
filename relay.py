# ファイル名: relay.py
import sys
import subprocess
import time

def run_remote(script_path):
    try:
        # 1. 実行したいファイルの中身を読み込む
        with open(script_path, 'r', encoding='utf-8') as f:
            code_content = f.read()

        print(f"🚀 {script_path} を GitHub Xeon へ転送中...")

        # 2. ghコマンドでワークフローを起動（引数としてコードを渡す）
        # ※ --raw-field を使うことで特殊文字のトラブルを防ぐ
        cmd = [
            'gh', 'workflow', 'run', 'remote_exec.yml',
            '--raw-field', f'code={code_content}'
        ]
        subprocess.run(cmd, check=True)

        print("⏳ サーバーが起動するのを待ってるぜ...")
        time.sleep(3) 

        # 3. ログを表示（リアルタイム監視）
        print("--- LOG START ---")
        subprocess.run(['gh', 'run', 'watch'], check=True)
        print("--- LOG END ---")

    except Exception as e:
        print(f"❌ エラー発生: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python relay.py [実行したいファイルのパス]")
    else:
        run_remote(sys.argv[1])