import stanza
import re

# ---------------------------
# 1. Init NLP pipeline
# ---------------------------
stanza.download('uk')
nlp = stanza.Pipeline('uk')

# ---------------------------
# 2. Input text
# ---------------------------
text = """
1. З "Поза собаки, яка дивиться вниз" зробіть крок правою ногою вперед до правої руки.
2. Зігніть праве коліно під прямим кутом, при цьому стегно буде паралельно підлозі, а коліно – над щиколоткою.
3. Натисніть лівою ногою на килимок.
4. Відведіть праве стегно назад і всередину до лівої п’ятки. 
Вдихніть, піднімаючи тулуб і згинаючи заднє коліно.
5. Покладіть руки нас стегна, щоб підтримувати таз, опускаючи куприк до килимка.
6. Підтягніть пупок вверх та таза.
Підніміть руки вверх. 
Робіть це, не випираючи ребра та таз вперед.
7. Випряміть ліве коліно, але лише настільки, щоб таз залишався нерухомим.
8. Затримайтесь у цій позі на 5 циклів дихання.
9. Опустіть руки на килимок та поверніться в «Поза собаки, яка дивиться вниз». Повторіть на іншу ногу.
"""

# прибрати цифри 
text = re.sub(r'^\s*\d+\.\s*', '', text, flags=re.MULTILINE)
text = re.sub(r'^\s*\.\s*', '', text, flags=re.MULTILINE)
text = re.sub(r'\s+', ' ', text).strip()

print(text)

# ---------------------------
# 3. NLP processing
# ---------------------------
doc = nlp(text)

# ---------------------------
# 4. Build dependency tree
# ---------------------------
def build_tree(sent):
    tree = {}
    for w in sent.words:
        tree.setdefault(w.head, []).append(w)
    return tree

# ---------------------------
# 5. Print + write tree with lemmas
# ---------------------------
def process_sentences(doc, output_file="dependency_trees_lemma.txt"):

    with open(output_file, "w", encoding="utf-8") as f:

        def write(line=""):
            f.write(line + "\n")

        def format_node(w):
#            return f"{w.text} → {w.lemma} ({w.deprel})"
             return f"{w.lemma} ({w.deprel})"
        def dfs(node, tree, prefix=""):
            children = tree.get(node.id, [])

            for i, child in enumerate(children):
                is_last = (i == len(children) - 1)
                connector = "└── " if is_last else "├── "

                line = prefix + connector + format_node(child)
                print(line)
                write(line)

                extension = "    " if is_last else "│   "
                dfs(child, tree, prefix + extension)

        # ---------------------------
        # 6. Process each sentence
        # ---------------------------
        for i, sent in enumerate(doc.sentences):

            header = f"\nSentence {i+1}: {sent.text}"
            print(header)
            write(header + "\n")

            tree = build_tree(sent)

            root = next(w for w in sent.words if w.deprel == "root")

            root_line = format_node(root)
            print(root_line)
            write(root_line)

            dfs(root, tree)

            print()
            write("\n")

# ---------------------------
# 6. Run pipeline
# ---------------------------
process_sentences(doc)