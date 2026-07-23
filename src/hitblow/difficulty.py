"""難易度（桁数）の選択"""


def select_digits():
    """3～9桁を選ばせて返す。"""

    while True:
        digits = input("難易度を選んでください（3～9桁）> ").strip()

        if not digits.isdigit():
            print("数字で入力してください。")
            continue

        digits = int(digits)

        if 3 <= digits <= 9:
            return digits

        print("3～9の整数を入力してください。")
