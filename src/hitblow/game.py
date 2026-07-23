"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret
from .cat import show_comment, show_clear_cat, reset_comments

def play(digits=3):
    from .difficulty import select_digits
    digits = select_digits()  # 難易度入力


    reset_comments()

    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")
    print("ヒントを見たいときは 'h' と入力してね")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====

    from .timer import start
    started_at = start()

    tries = 0
    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        from .hint import hint
        if guess == "h":
            print(hint(secret))
            continue

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")
        # ガヤを入れる

        if hit == digits:

            show_clear_cat()

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====

            from .timer import elapsed_since
            elapsed = elapsed_since(started_at)
            print(f"クリア時間：{elapsed:.1f} 秒")

            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break

        else:
            show_comment(hit, blow, digits)
