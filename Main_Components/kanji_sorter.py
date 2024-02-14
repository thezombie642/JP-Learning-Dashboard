import json

def stroke_map(k_dict):
    stroke_map = {i : [] for i in range(1, 35)}
    for k, v in k_dict.items():
        stroke_map[int(v['strokes'])].append(k)
    return stroke_map

def word_map(k_dict):
    key_map = {}
    for k, v in k_dict.items():
        keyword = "nan" if not v['meanings'] else v['meanings'][0].lower()
        try:
            key_map[keyword].append(k)
        except:
            key_map[keyword] = [k]
    return key_map

def create_helper_files():
    out_stroke = {}
    out_keyword = {}
    with open("kanji_with_keyword.json", "+r") as kanji_unsorted:
        kanji_dict = json.load(kanji_unsorted)  
        print(kanji_dict)
        out_stroke = stroke_map(kanji_dict)
        out_keyword = word_map(kanji_dict)

    with open("kanji_by_stroke.json", "+w", encoding = "utf8") as kanji_stroke:
        json.dump(out_stroke, kanji_stroke, ensure_ascii=False)

    with open("kanji_by_keyword.json", "+w", encoding = "utf8") as kanji_keyword:
        json.dump(out_keyword, kanji_keyword, ensure_ascii=False)

if __name__ == '__main__':
    create_helper_files()