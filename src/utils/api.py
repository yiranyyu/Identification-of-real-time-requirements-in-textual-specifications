from utils import *


def fetch(number_of_sentences: int, doc_list: tuple = tuple(range(1, 49)), keywords: list = None):
    """
        fetch sentences from doc_list. (might with keywords)

        :param number_of_sentences:
        :param doc_list: list of int, [1,2,3, ...]
        :param keywords: list of string, [keyword1, keyword2, ...], the keyword used to select sentence
        :return: list of sentences, which are selected from the doc_list
            type: list of string [string, string, ...] -> [sentence, sentence, ...]
    """
    keywords = [str()] if keywords is None else keywords
    text = Fetcher.get_total_text(doc_list, keywords)
    random.shuffle(text)

    return text[:number_of_sentences]


def change_ratio(origin, division, ratio, mode):
    """
        change the ratio of difference type of sentences 

        :param origin: list (of string), format is sentence😂type😂description
        :param ratio: list, [elem_1, elem_2]
        :param division: list of list, [[], []]
        :param mode: string, "subSample" or "oversample"
        :return: text that suitable for the :param ratio
            type: same as origin
    """
    # text : map, from sentences to 0/1/2
    text = RatioChanger.get_map(origin)

    # [[strings in type0], [strings in type1], [strings in type2]]
    typed_text = RatioChanger.partition(text)

    part1 = []
    part2 = []
    for i in division[0]:
        part1.extend(typed_text[i])
    for i in division[1]:
        part2.extend(typed_text[i])

    now_ratio = [len(part1), len(part2)]
    now_text = [part1, part2]

    base = 0
    the_other = 1

    if mode == "subSample":
        RatioChanger.adjust_sub(now_ratio, ratio, now_text, base, the_other)
    elif mode == "overSample":
        RatioChanger.adjust_over(now_ratio, ratio, now_text, base, the_other)

    return now_text[0] + now_text[1]


def test_fetch():
    print(fetch(10, (1, 2)))


def test_change_ratio():
    text = [
        "1_1😂1😂", "2_1😂1😂", "3_1😂1😂", "4_1😂1😂", "5_1😂1😂", "6_1😂1😂", "7_1😂1😂", "8_1😂1😂", "9_1😂1😂",
        "10_1😂1😂",
        "1_0😂0😂", "2_0😂0😂", "3_0😂0😂", "4_0😂0😂", "5_0😂0😂", "6_0😂0😂", "7_0😂0😂", "8_0😂0😂", "9_0😂0😂",
        "10_0😂0😂",
        "1_2😂2😂", "2_2😂2😂", "3_2😂2😂", "4_2😂2😂", "5_2😂2😂", "6_2😂2😂", "7_2😂2😂", "8_2😂2😂", "9_2😂2😂",
        "10_2😂2😂",
    ]
    print(change_ratio(text, [[0, 1], [2]], [13, 4], "overSample"))
    print(change_ratio(text, [[0, 1], [2]], [13, 17], "subSample"))


if __name__ == "__main__":
    #test_fetch()
    test_change_ratio()
