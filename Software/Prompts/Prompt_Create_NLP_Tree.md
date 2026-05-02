# PROMPT: Tree → Semantic Triples Extractor (PTCF)

## PERSONA
Ти — експерт з Computational Linguistics та Semantic Parsing.
Ти спеціалізуєшся на перетворенні dependency trees (Universal Dependencies) у семантичні knowledge graphs та OpenIE-триплети.

## TASKS
1) Проаналізувати dependency tree речення.
2) Виявити:
- головні події (ROOT + предикати)
- суб’єкти (nsubj / nsubj:pass)
- об’єкти (obj / obl / nmod)
- координовані елементи (conj)
- вкладені події (xcomp / advcl)
- просторові/часові відношення (case + obl)
3) Розгорнути subtree у повні семантичні сутності.
4) Перетворити структуру у множину семантичних триплетів.
5) Правила:
- НЕ втрачати елементи списків (conj).
- Розгортати noun phrases (nmod, compound, amod).
- Обробляти еліптичні структури (orphan).
- Імпліцитний підмет = "implicit_user", якщо відсутній.
- Не залишати вузли без семантичної інтерпретації.


Sentence 2: Встаньте, стопи паралельно, основи великих пальців ніг торкаються, а п’яти злегка розведені.

Встаньте (ROOT)
├── стопи (nsubj)
├── паралельно (advmod)
│   └── , (punct)
├── торкаються (parataxis)
│   ├── , (punct)
│   ├── основи (nsubj)
│   │   └── пальців (nmod)
│   │       ├── великих (amod)
│   │       └── ніг (nmod)
│   └── розведені (conj)
│       ├── , (punct)
│       ├── а (cc)
│       ├── п’яти (nsubj)
│       └── злегка (advmod)
└── . (punct)

Sentence 4: Підніміть і розведіть пальці ніг віялом, а потім опустіть їх на килимок, щоб створити широку міцну основу.

Підніміть (ROOT)
├── розведіть (conj)
│   ├── і (cc)
│   ├── пальці (obj)
│   │   └── ніг (nmod)
│   └── віялом (obl)
├── опустіть (conj)
│   ├── , (punct)
│   ├── а (cc)
│   ├── потім (advmod)
│   ├── їх (obj)
│   ├── килимок (obl)
│   │   └── на (case)
│   └── створити (advcl)
│       ├── , (punct)
│       ├── щоб (mark)
│       └── основу (obj)
│           ├── широку (amod)
│           └── міцну (amod)
└── . (punct)

Sentence 6: Активуйте квадратний м’яз і потягніть його вверх, змушуючи колінні чашечки підніматися.

Активуйте (ROOT)
├── м’яз (obj)
│   └── квадратний (amod)
├── потягніть (conj)
│   ├── і (cc)
│   ├── його (obj)
│   ├── вверх (advmod)
│   └── змушуючи (advcl)
│       ├── , (punct)
│       ├── чашечки (obj)
│       │   └── колінні (amod)
│       └── підніматися (xcomp)
└── . (punct)


Sentence 8: Поверніть обидва стегна всередину, створюючи розширення сідниць.

Поверніть (ROOT)
├── стегна (obj)
│   └── обидва (nummod)
├── всередину (advmod)
├── створюючи (advcl)
│   ├── , (punct)
│   └── розширення (obj)
│       └── сідниць (nmod)
└── . (punct)


Sentence 10: Не висуваючи вперед нижні передні ребра, підніміть грудну клітку вверх.

підніміть (ROOT)
├── висуваючи (advcl)
│   ├── Не (advmod)
│   ├── вперед (advmod)
│   ├── ребра (obj)
│   │   ├── нижні (amod)
│   │   └── передні (amod)
│   └── , (punct)
├── клітку (obj)
│   └── грудну (amod)
├── вверх (advmod)
└── . (punct)


Sentence 11: Підніміть плечі вверх, а потім відведіть їх назад і опустіть.

Підніміть (ROOT)
├── плечі (obj)
├── вверх (advmod)
├── відведіть (conj)
│   ├── , (punct)
│   ├── а (cc)
│   ├── потім (advmod)
│   ├── їх (obj)
│   ├── назад (advmod)
│   └── опустіть (conj)
│       └── і (cc)
└── . (punct)


Sentence 12: Дозвольте вашим лопаткам потягнутися одна до одної та вниз.

Дозвольте (ROOT)
├── лопаткам (obj)
│   └── вашим (det)
├── потягнутися (xcomp)
│   ├── одна (obl)
│   │   └── одної (flat:abs)
│   │       └── до (case)
│   └── вниз (advmod)
│       └── та (cc)
└── . (punct)

Sentence 14: Зберігайте природні вигни хребта.

Зберігайте (ROOT)
├── вигни (obj)
│   ├── природні (amod)
│   └── хребта (nmod)
└── . (punct)

Sentence 16: Підтягніть живіт, злегка втягнувши його.

Підтягніть (ROOT)
├── живіт (obj)
├── втягнувши (advcl)
│   ├── , (punct)
│   ├── злегка (advmod)
│   └── його (obj)
└── . (punct)

Sentence 18: Руки звисають природньо, злегка зігніть лікті, долоні поверніть вперед.

звисають (ROOT)
├── Руки (nsubj)
├── природньо (advmod)
├── зігніть (conj)
│   ├── , (punct)
│   ├── злегка (advmod)
│   └── лікті (obj)
├── поверніть (conj)
│   ├── , (punct)
│   ├── долоні (obj)
│   └── вперед (advmod)
│       └── 9 (appos)
│           └── . (punct)
└── . (punct)


Sentence 19: Збалансуйте голову прямо над стегнами та дивіться прямо.

Збалансуйте (ROOT)
├── голову (obj)
├── прямо (advmod)
├── стегнами (obl)
│   └── над (case)
├── дивіться (conj)
│   ├── та (cc)
│   └── прямо (advmod)
└── . (punct)

Sentence 20: Шия довга, підборіддя не опущене й не підняте, а маківка тягнеться до стелі.

довга (ROOT)
├── Шия (nsubj)
├── опущене (parataxis)
│   ├── , (punct)
│   ├── підборіддя (nsubj)
│   ├── не (advmod)
│   └── підняте (conj)
│       ├── й (cc)
│       └── не (advmod)
├── тягнеться (conj)
│   ├── , (punct)
│   ├── а (cc)
│   ├── маківка (nsubj)
│   └── стелі (obl)
│       └── до (case)
└── . (punct)

Sentence 22: Перевіривши всі точки правильного положення тіла, зробіть від 5 до 10 циклів дихання, утримуючи себе в цьому положенні.

зробіть (ROOT)
├── Перевіривши (advcl)
│   ├── точки (obj)
│   │   ├── всі (det)
│   │   └── положення (nmod)
│   │       ├── правильного (amod)
│   │       └── тіла (nmod)
│   └── , (punct)
├── циклів (obj)
│   ├── 5 (nummod:gov)
│   │   ├── від (case)
│   │   └── 10 (flat:range)
│   │       └── до (case)
│   └── дихання (nmod)
├── утримуючи (advcl)
│   ├── , (punct)
│   ├── себе (obj)
│   └── положенні (obl)
│       ├── в (case)
│       └── цьому (det)
└── . (punct)


## CONTEXT:
1) Вхідні дані — це dependency tree у форматі:
word (relation)
├── child (relation)
Або список вузлів із залежностями:
word → head + deprel
2) Це не поверхневий текст, а синтаксична структура Universal Dependencies.
3) Мета — отримати semantic representation (knowledge graph level).
4) INPUT EXAMPLE
control (ROOT)
├── players (nsubj)
│   └── Two (nummod)
├── characters (obj)
└── arena (obl)
    └── in (case)
5) OUTPUT EXAMPLE
(players, control, characters)
(control, location, arena)
(arena, relation, in)
(players, quantity, 2)

## FORMAT:
1) Поверни результат у вигляді:
(subject, predicate, object)
2) Додаткові семантичні відношення (за наявності):
(entity, attribute, value)
(event, modifier, value)
(event1, relation, event2)
3) Правила нормалізації:
- об’єднуй coordination (conj) у окремі триплети
- розкривай noun phrases (nmod, compound)
- розділяй embedded events (xcomp, advcl)
- case markers перетворюй у відношення
