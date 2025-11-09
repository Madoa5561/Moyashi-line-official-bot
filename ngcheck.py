import re
import requests
from bs4 import BeautifulSoup
from pykakasi import kakasi

class ContainNgWordError(Exception):
    def __init__(self, message):
        self.message = message

class NgWordSystem:
    def __init__(self):
        self.processed_ng_words = self.process_ng_words()
 
    def get_ng_words(self):
        wikipedia_url = "https://ja.wikipedia.org/wiki/%E6%80%A7%E9%A2%A8%E4%BF%97%E7%94%A8%E8%AA%9E%E4%B8%80%E8%A6%A7" # このサイトからNGワードを抽出
        ng_words = self.get_wikipedia_terms(wikipedia_url)
        ng_words = ng_words[1:164]

        return ng_words

    def process_ng_words(self):
        self.kakasi = kakasi()
        self.kakasi.setMode('H', 'a')
        self.kakasi.setMode('K', 'a')
        self.kakasi.setMode('J', 'a')

        conv = self.kakasi.getConverter()
        new_ng_words = []
        for word in self.get_ng_words():
            new_ng_words.append(conv.do(word).lower()) 
        processed_ng_words = []
        for word in new_ng_words:
            parts = list(filter(None, re.split('[（）、()]', word)))
            processed_ng_words.extend(parts)
        add_ng_list = ['bdsm', 'smsadizumu', '4545', "0721", '1919','lime','lime交換','hしよ','せkk','せっくs','せっkusu','ふぁっきゅー','fakkyu-','ぉなに','ぁなる','fuckyou','เหี้ย','เชี่ย','ไอ้','คำด่า','ด่า','810','line交換','line',"きみ","どこすみ？","どこ住み","dokosumi","セクス","せくす","ぱわはら","manko","mannko","sekusu",'らいん','ライン',"らいん交換","https://","line://","http://",".com","うんち","fuck","fuckin","unti","yazyuusenpai","snapchat","fackbook","sekkusu","onani","pussy","dick","tinko","tinpo","tintin","otintin","lime"]   # NGワードを追加
        processed_ng_words.extend(add_ng_list)
        processed_ng_words = list(set(processed_ng_words))

        return processed_ng_words

    def get_wikipedia_terms(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        terms = []
        term_section = soup.find('div', {'id': 'mw-content-text'})
        for li in term_section.find_all('li'):
            term = li.get_text(strip=True)
            terms.append(term)

        return terms    



    def detect(self, text):
        self.text = text
        self.text = self.text.replace(" ", "")
        self.text = self.text.replace("　", "")
        self.text = self.text.replace("１", "")
        self.text = self.text.replace("２", "")
        self.text = self.text.replace("３", "")
        self.text = self.text.replace("４", "")
        self.text = self.text.replace("５", "")
        self.text = self.text.replace("６", "")
        self.text = self.text.replace("７", "")
        self.text = self.text.replace("８", "")
        self.text = self.text.replace("９", "")
        self.text = self.text.replace("０", "")
        self.text = self.text.replace("、", "")
        self.text = self.text.replace("。", "")
        self.text = self.text.replace("！", "")
        self.text = self.text.replace("？", "")
        self.text = self.text.translate(str.maketrans(
            'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
            'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
            '１２３４５６７８９０'
            '！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～',
            'abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '1234567890'
            '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        ))
        katakana_to_hiragana = str.maketrans(
            'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンァィゥェォッャュョｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯｬｭｮ',
            'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんぁぃぅぇぉっゃゅょあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんぁぃぅぇぉっゃゅょ'
        )
        self.text = self.text.translate(katakana_to_hiragana)
        self.text = self.text.replace("ぁ", "")
        self.text = self.text.replace("ぃ", "")
        self.text = self.text.replace("ぅ", "")
        self.text = self.text.replace("ぇ", "")
        self.text = self.text.replace("ぉ", "")
        self.text = self.text.replace("っ", "")
        self.text = self.text.replace("ゃ", "")
        self.text = self.text.replace("ゅ", "")
        self.text = self.text.replace("ょ", "")
        self.text = self.text.replace("ゎ", "")
        self.text = self.text.replace("!", "")
        self.text = self.text.replace("?", "")
        self.text = self.text.replace("'", "")
        self.text = self.text.replace("\"", "")
        self.text = self.text.replace("#", "")
        self.text = self.text.replace("$", "")
        self.text = self.text.replace("%", "")
        self.text = self.text.replace("&", "")
        self.text = self.text.replace("(", "")
        self.text = self.text.replace(")", "")
        self.text = self.text.replace("*", "")
        self.text = self.text.replace("+", "")
        self.text = self.text.replace(",", "")
        self.text = self.text.replace("-", "")
        self.text = self.text.replace(".", "")
        self.text = self.text.replace("/", "")
        self.text = self.text.replace(":", "")
        self.text = self.text.replace(";", "")
        self.text = self.text.replace("<", "")
        self.text = self.text.replace("=", "")
        self.text = self.text.replace(">", "")
        self.text = self.text.replace("@", "")
        self.text = self.text.replace("[", "")
        self.text = self.text.replace("\\", "")
        self.text = self.text.replace("]", "")
        self.text = self.text.replace("^", "")
        self.text = self.text.replace("_", "")
        self.text = self.text.replace("`", "")
        self.text = self.text.replace("{", "")
        self.text = self.text.replace("|", "")
        self.text = self.text.replace("}", "")
        self.text = self.text.replace("~", "")
        self.text = self.text.replace("！", "")
        self.text = self.text.replace("？", "")
        self.text = self.text.replace("＃", "")
        self.text = self.text.replace("＄", "")
        self.text = self.text.replace("％", "")
        self.text = self.text.replace("＆", "")
        self.text = self.text.replace("（", "")
        self.text = self.text.replace("）", "")
        self.text = self.text.replace("＊", "")
        self.text = self.text.replace("＋", "")
        self.text = self.text.replace("，", "")
        self.text = self.text.replace("－", "")
        self.text = self.text.replace("．", "")
        self.text = self.text.replace("／", "")
        self.text = self.text.replace("：", "")
        self.text = self.text.replace("；", "")
        self.text = self.text.replace("＜", "")
        self.text = self.text.replace("＝", "")
        self.text = self.text.replace("＞", "")
        self.text = self.text.replace("＠", "")
        self.text = self.text.replace("［", "")
        self.text = self.text.replace("￥", "")
        self.text = self.text.replace("］", "")
        self.text = self.text.replace("＾", "")
        self.text = self.text.replace("＿", "")
        self.text = self.text.replace("｀", "")
        self.text = self.text.replace("｛", "")
        self.text = self.text.replace("｜", "")
        self.text = self.text.replace("｝", "")
        self.text = self.text.replace("～", "")
        self.text = self.text.lower()
        self.kakasi = kakasi()
        self.kakasi.setMode('H', 'a')
        self.kakasi.setMode('K', 'a')
        self.kakasi.setMode('J', 'a')

        conv = self.kakasi.getConverter()
        ngs = 0
        for i in self.processed_ng_words:
            if i in conv.do(self.text) and i != "":
                  ngs += 1
        if not all('\u0020' <= char <= '\u007e' or '\u3040' <= char <= '\u30ff' for char in self.text):
            ngs += 1
        if ngs == 0:
            return False
        else:
            return True
