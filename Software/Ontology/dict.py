BODY_MAP = {
    "нога": ["hip","knee","ankle","heel","foot_index"],
    "рука": ["shoulder","elbow","wrist"],
    "коліно": ["knee"],
    "таз": ["left_hip","right_hip"],
    "спина": ["shoulder","hip"]
}

ACTION_GRAPH = {

    # переміщення
    "зробити": "STEP",
    "крокувати": "STEP",

    # згинання / випрямлення
    "зігнути": "BEND",
    "випрямити": "STRAIGHT",
    "розігнути": "STRAIGHT",

    # підйом / опускання
    "піднімати": "RAISE",
    "опускати": "LOWER",

    # напрям руху
    "відвести": "MOVE_AWAY",
    "повернути": "ROTATE",
    "повернутися": "RETURN",

    # тиск / опора
    "натиснути": "PRESS",
    "спиратися": "SUPPORT",

    # утримання
    "тримати": "HOLD",
    "залишатися": "HOLD",
    "затриматися": "HOLD",

    # дихання
    "вдихнути": "INHALE",
    "видихнути": "EXHALE",

    # повтор
    "повторити": "REPEAT"
}

SPATIAL_GRAPH = {

    "вперед": "FORWARD",
    "назад": "BACKWARD",

    "вгору": "UP",
    "вверх": "UP",
    "вниз": "DOWN",

    "всередину": "INWARD",
    "назовні": "OUTWARD",

    "до": "TOWARD",
    "на": "ON",
    "над": "ABOVE",

    "паралельно": "PARALLEL",
    "перпендикулярно": "PERPENDICULAR"
}

CONSTRAINT_GRAPH = {

    # кути
    "прямий кут": {
        "type": "ANGLE",
        "value": 90
    },

    # вирівнювання
    "паралельно підлозі": {
        "type": "ALIGNMENT",
        "axis": "HORIZONTAL"
    },

    # стабільність
    "нерухомий таз": {
        "type": "STABILITY",
        "target": "PELVIS"
    },

    # положення коліна
    "коліно над щиколоткою": {
        "type": "ALIGNMENT",
        "relation": "vertical_stack"
    },

    # дихання
    "циклів дихання": {
        "type": "DURATION",
        "unit": "breath_cycle"
    }
}
