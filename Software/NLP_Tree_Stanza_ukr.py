import stanza

stanza.download('uk')
nlp = stanza.Pipeline('uk')

text = """
1. Встаньте, стопи паралельно, основи великих пальців ніг торкаються, а п’яти злегка розведені.
2. Підніміть і розведіть пальці ніг віялом, а потім опустіть їх на килимок, щоб створити широку міцну основу.
3. Активуйте квадратний м’яз і потягніть його вверх, змушуючи колінні чашечки підніматися.
4. Поверніть обидва стегна всередину, створюючи розширення сідниць.
5. Не висуваючи вперед нижні передні ребра, підніміть грудну клітку вверх. Підніміть плечі вверх, а потім відведіть їх назад і опустіть.
Дозвольте вашим лопаткам потягнутися одна до одної та вниз.
6. Зберігайте природні вигни хребта.
7. Підтягніть живіт, злегка втягнувши його.
8. Руки звисають природньо, злегка зігніть лікті, долоні поверніть вперед.
9. Збалансуйте голову прямо над стегнами та дивіться прямо. 
Шия довга, підборіддя не опущене й не підняте, а маківка тягнеться до стелі.
10. Перевіривши всі точки правильного положення тіла, зробіть від 5 до 10 циклів дихання, утримуючи себе в цьому положенні.
"""

doc = nlp(text)


def extract_triples(sent):
    root = None
    subj = None
    obj = None

    triples = []

    for w in sent.words:
        if w.deprel == "root":
            root = w
        elif w.deprel == "nsubj":
            subj = w
        elif w.deprel == "obj":
            obj = w

    if root and subj and obj:
        triples.append((subj.text, root.text, obj.text))

    return triples

def build_tree(sent):
    """
    Будує структуру head → children
    """
    tree = {}

    for w in sent.words:
        tree.setdefault(w.head, []).append(w)

    return tree


def print_ascii_tree(sent):
    tree = build_tree(sent)

    root = next(w for w in sent.words if w.deprel == "root")

    def dfs(node, prefix=""):
        children = tree.get(node.id, [])

        for i, child in enumerate(children):
            is_last = (i == len(children) - 1)

            connector = "└── " if is_last else "├── "

            print(prefix + connector + f"{child.text} ({child.deprel})")

            extension = "    " if is_last else "│   "
            dfs(child, prefix + extension)

    print(f"{root.text} (ROOT)")
    dfs(root)

with open("dependency_trees.txt", "w", encoding="utf-8") as f:

    for i, sent in enumerate(doc.sentences):
        f.write(f"\nSentence {i+1}: {sent.text}\n\n")

        # тимчасово перенаправляємо print у файл
        def write_line(line=""):
            f.write(line + "\n")

        tree = build_tree(sent)
        root = next(w for w in sent.words if w.deprel == "root")

        def dfs(node, prefix=""):
            children = tree.get(node.id, [])

            for i, child in enumerate(children):
                is_last = (i == len(children) - 1)
                connector = "└── " if is_last else "├── "

                write_line(prefix + connector + f"{child.text} ({child.deprel})")

                extension = "    " if is_last else "│   "
                dfs(child, prefix + extension)

        write_line(f"{root.text} (ROOT)")
        dfs(root)

        f.write("\n")