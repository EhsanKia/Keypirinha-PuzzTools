import re

import keypirinha as kp
import keypirinha_util as kpu

_SORTS = {
    'alphabetical': lambda x: '\n'.join(sorted(x.split('\n'))),
    'by length': lambda x: '\n'.join(sorted(x.split('\n'), key=len)),
    'reverse': lambda x: '\n'.join(reversed(x.split('\n'))),
}

_NUTRIMATICS = {
    'from ANSWERIZE': lambda x: x.lower().replace('?', 'A'),
    'add A* between': lambda x: 'A*' + 'A*'.join(x) + 'A*',
    'add ?': lambda x: ''.join(f'{c}?' for c in x),
    'from enumeration': lambda x: ' '.join(f'A{{{n}}}' for n in re.findall('\d+', x)),
}

_TRANSFORMS = {
    'alphabet': lambda _: 'abcdefghijklmnopqrstuvwxyz',
    'answerize': lambda s: re.sub('[^A-Z0-9]', '', s.upper()),
    'length': len,
    'lowercase': str.lower,
    'nutrimatic': _NUTRIMATICS,
    'reverse': lambda x: x[::-1],
    'sort': _SORTS,
    'transpose': lambda x: '\n'.join(''.join(line) for line in zip(*x.split('\n'))),
    'uppercase': str.upper,
}


class PuzzTools(kp.Plugin):
    """Plugin with useful tools for puzzle solvers."""

    DIRECT = kp.ItemCategory.USER_BASE + 1
    NESTED = kp.ItemCategory.USER_BASE + 2

    def on_catalog(self) -> None:
        catalog = list(self._build_catalog())
        self.set_catalog(catalog)

    def on_execute(self, item, action):
        input_data = kpu.get_clipboard()
        transform_name, _, subtransform_name = item.target().partition('.')
        transform = _TRANSFORMS[transform_name]
        if subtransform_name:
            transform = transform[subtransform_name]
        result = str(transform(input_data))
        kpu.set_clipboard(result)

    def on_suggest(self, user_input, items_chain):
        if not items_chain:
            return
        item = items_chain[0]
        if item.category() != self.NESTED:
            return

        suggestions = []
        transform_name = item.target()
        for subtransform_name in _TRANSFORMS[transform_name]:
            suggestions.append(
                self.create_item(
                    category=self.DIRECT,
                    label=subtransform_name.title(),
                    short_desc=f'{transform_name} {subtransform_name}',
                    target=f'{transform_name}.{subtransform_name}',
                    args_hint=kp.ItemArgsHint.FORBIDDEN,
                    hit_hint=kp.ItemHitHint.KEEPALL)
            )
        self.set_suggestions(suggestions)

    def _build_catalog(self):
        for transform_name, transform in _TRANSFORMS.items():
            category, args_hint = self.DIRECT, kp.ItemArgsHint.FORBIDDEN
            if isinstance(transform, dict):
                category, args_hint = self.NESTED, kp.ItemArgsHint.REQUIRED

            yield self.create_item(
                category=category,
                label=transform_name.title(),
                short_desc=f'Converts clipboard into {transform_name}',
                target=transform_name,
                args_hint=args_hint,
                hit_hint=kp.ItemHitHint.NOARGS)