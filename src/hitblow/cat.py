import random

# 一度表示したHit数を記録
_shown_hits = set()

def reset_comments():
    """ゲーム開始時に呼ぶ"""
    global _shown_hits
    _shown_hits = set()

# --- 猫たち -------------------------------------------------

def show_encourage_cat():
    print(r"""
 /\_/\  
(=^.^=)  ＜ もう少し！
 /   \
""")


def show_close_cat():
    print(r"""
 /\_/\ 
(=｀ω´=)  ＜ かなり近づいてるぞ！
 /   \
""")


def show_clear_cat():
    print(r"""
 /\_/\ 
(≧ω≦)  ＜ 正解！！お見事！！
 /   \
""")


def show_surprised_cat():
    print(r"""
      ___________________
     < おっ、やるやん！ >
      -------------------
             \
              \
 /\_/\
( ﾟдﾟ )
 /   \
""")


def show_no_hit_cat():
    print(r"""
 /\_/\ 
(；ﾟДﾟ)  ＜ 逆に才能ある。
 /   \
""")


def show_zero_blow_cat():
    print(r"""
 /\_/\ 
( ˘ω˘ )  ＜ その数字、今日休みらしい。
 /   \
""")


def show_ignore_cat():
    print(r"""
 /\_/\ 
( ˘ω˘ )  ＜ 今のは見なかったことにしよう。
 /   \
""")


def show_two_hit_cat():
    print(r"""
 /\_/\ 
(๑•̀ㅂ•́)و✧  ＜ 犯人はこの中にいる！
 /   \
""")


def show_many_blow_cat():
    print(r"""
 /\_/\ 
(・∀・)  ＜ 並び替えたら世界変わるぞ。
 /   \
""")


def show_one_hit_cat():
    print(r"""
 /\_/\ 
(=^.^=)  ＜ 1つ当たってるぞ！
 /   \
""")


def show_accident_cat():
    print(r"""
 /\_/\ 
( ˘ω˘ )  ＜ それ偶然じゃない？
 /   \
""")


def show_almost_wrong_cat():
    print(r"""
 /\_/\ 
(・∀・)  ＜ 惜しい。でも惜しいだけ。
 /   \
""")


def show_cpu_laugh_cat():
    print(r"""
 /\_/\ 
(＾▽＾)  ＜ CPUが笑ってるぞ。
 /   \
""")


def show_spirit_cat():
    print(r"""
 /\_/\ 
( •̀ω•́ )  ＜ ヒント：気合い。
 /   \
""")


def show_calm_cat():
    print(r"""
 /\_/\ 
(=^.^=)  ＜ 落ち着け、まだ序盤だ。
 /   \
""")


# --- 演出グループ ------------------------------------------

NO_HIT = [
    show_no_hit_cat,
    show_ignore_cat,
    show_cpu_laugh_cat,
]

ONE_HIT = [
    show_one_hit_cat,
    show_accident_cat,
    show_encourage_cat,
]

TWO_HIT = [
    show_two_hit_cat,
    show_encourage_cat,
]
ALMOST = [
    show_surprised_cat,
    show_close_cat,
]
MANY_BLOW = [
    show_many_blow_cat,
    show_almost_wrong_cat,
]

ZERO_BLOW = [
    show_zero_blow_cat,
    show_spirit_cat,
]

ENCOURAGE = [
    show_encourage_cat,
    show_spirit_cat,
    show_calm_cat,
]

HIT_COMMENTS = {
    1: ONE_HIT,
    2: TWO_HIT,
    # 3: THREE_HIT,
    # 4: FOUR_HIT,
}

# --- コメント表示 ------------------------------------------

def show_comment(hit, blow, digits):
    # 初めてそのHit数になったときだけ
    if 1 <= hit < digits and hit not in _shown_hits:
        _shown_hits.add(hit)

        # リーチならALMOST
        if hit == digits - 1:
            random.choice(ALMOST)()

        # それ以外はHit数に応じた演出
        else:
            random.choice(HIT_COMMENTS.get(hit, ENCOURAGE))()

        return

    # 0Hit0Blow
    if hit == 0 and blow == 0:
        random.choice(NO_HIT)()
        return

    # Blowが多い
    if blow >= 2:
        random.choice(MANY_BLOW)()
        return

    # Blowが0
    if blow == 0:
        random.choice(ZERO_BLOW)()
        return

    # その他
    random.choice(ENCOURAGE)()