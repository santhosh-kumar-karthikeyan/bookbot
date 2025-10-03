def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> dict[str, int]:
    from collections import Counter   
    count_map = Counter([c.lower() for w in text.split() for c in w])
    return dict(count_map)

def get_sorted_list(count_map: dict[str,int]) :
    result = []
    for key, value in count_map.items():
        result.append({
            "char" : key,
            "num" : value
        })
    result.sort(key = lambda res: res["num"], reverse = True)
    return result