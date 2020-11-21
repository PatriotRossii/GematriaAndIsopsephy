STANDARD_ENCODING = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 20,
    "ל": 30,
    "מ": 40,
    "נ": 50,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "צ": 90,
    "ק": 100,
    "ר": 200,
    "ש": 300,
    "ת": 400
}

FINAL_ENCODING = {
    "ך": 500,
    "ם": 600,
    "ן": 700,
    "ף": 800,
    "ץ": 900
}


class GematriaDecoder:
    @staticmethod
    def decode_word(word: str) -> int:
        last_idx = len(word) - 1
        return sum([FINAL_ENCODING[ch] if (ch in FINAL_ENCODING and idx == last_idx) else STANDARD_ENCODING[ch]
                    for idx, ch in enumerate(word)])