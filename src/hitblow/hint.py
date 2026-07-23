"""ヒント機能を提供するモジュール。"""

import random


def hint(secret):
    """secret の中からランダムに1文字を選んでヒントとして返す。"""
    chosen = random.choice(secret)
    return f"【ヒント】答えには '{chosen}' という数字が含まれています。"