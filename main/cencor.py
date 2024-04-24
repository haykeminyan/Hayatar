import json
import os
from pathlib import Path

PROFANE_WORD_LIST_PATH = Path("profanity.json")

with open(
    os.path.join(os.path.dirname(__file__), PROFANE_WORD_LIST_PATH), "r"
) as _profane_word_list:
    PROFANE_WORD_LIST = json.load(_profane_word_list)


def censor_profanity(text: str, censor: str = "*") -> str:
    """Censors all profane words with the provided censor"""

    split_text: list = text.split()
    final_text: str = " ".join(split_text)

    if len(split_text) < len(PROFANE_WORD_LIST):
        for word in split_text:
            if word.lower() in PROFANE_WORD_LIST:
                final_text = final_text.replace(word, censor * len(word))
    else:
        for word in PROFANE_WORD_LIST:
            if word in split_text:
                final_text = final_text.replace(word, censor * len(word))

    return final_text
