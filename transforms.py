import re
from typing import Callable, Iterable

Grid = Iterable[Iterable[str]]
GridTransform = Callable[[Grid], Grid]


def make_grid_transform(grid_transform: GridTransform) -> Callable[[str], str]:
    """Returns a transform that applies the given grid transform to the input text."""
    def transform(data: str) -> str:
        has_tab = '\t' in data
        new_line = '\r\n' if '\r\n' in data else '\n'
        grid = [l.split('\t') if has_tab else list(l) for l in data.split(new_line)]
        new_grid = grid_transform(grid)
        return new_line.join(('\t' if has_tab else '').join(line) for line in new_grid)
    return transform

_SORTS = {
    'alphabetical': lambda x: '\n'.join(sorted(x.split('\n'))),
    'by length': lambda x: '\n'.join(sorted(x.split('\n'), key=len)),
    'reverse': lambda x: '\n'.join(reversed(x.split('\n'))),
}

_NUTRIMATICS = {
    'from ANSWERIZE': lambda x: x.lower().replace('?', 'A'),
    'add A* between': lambda x: 'A*' + 'A*'.join(x) + 'A*',
    'add ?': lambda x: ''.join(f'{c}?' for c in x),
    'from enumeration': lambda x: ' '.join(f'A{{{n}}}' for n in re.findall(r'\d+', x)),
}

TRANSFORMS = {
    'alphabet': lambda _: 'abcdefghijklmnopqrstuvwxyz',
    'answerize': lambda x: re.sub('[^A-Z0-9]', '', x.upper()),
    'kebabcase': lambda x: re.sub(r'\s|(\B)([A-Z])', r'-\2', x).lower(),
    'length': len,
    'lowercase': str.lower,
    'nutrimatic': _NUTRIMATICS,
    'reverse': lambda x: x[::-1],
    'rotate': make_grid_transform(lambda x: zip(*reversed(x))),
    'snakecase': lambda x: re.sub(r'\s|(\B)([A-Z])', r'_\2', x).lower(),
    'sort': _SORTS,
    'transpose': make_grid_transform(lambda x: zip(*x)),
    'unique': lambda x: ''.join(set(x)),
    'uppercase': str.upper,
}
