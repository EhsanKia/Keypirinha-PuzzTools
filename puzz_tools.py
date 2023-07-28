from . import transforms
import keypirinha as kp
import keypirinha_util as kpu


class PuzzTools(kp.Plugin):
    """Plugin with useful tools for puzzle solvers."""

    DIRECT = kp.ItemCategory.USER_BASE + 1
    NESTED = kp.ItemCategory.USER_BASE + 2

    def on_catalog(self) -> None:
        catalog = list(self._build_catalog())
        self.set_catalog(catalog)

    def on_execute(self, item, unused_action):
        input_data = item.raw_args() or kpu.get_clipboard()
        transform_name, _, subtransform_name = item.target().partition('.')
        transform = transforms.TRANSFORMS[transform_name]
        if subtransform_name:
            transform = transform[subtransform_name]
        result = str(transform(input_data))
        kpu.set_clipboard(result)

    def on_suggest(self, user_input, items_chain):
        if not items_chain:
            return
        item = items_chain[0]

        if item.category() == self.DIRECT:
            # User is providing a custom input, set input in item arguments.
            new_item = item.clone()
            new_item.set_args(user_input)
            self.set_suggestions([new_item], kp.Match.ANY, kp.Sort.NONE)
        elif item.category() == self.NESTED:
            # User is in a nested transform menu, list all subtransforms
            suggestions = []
            transform_name = item.target()
            for subtransform_name in transforms.TRANSFORMS[transform_name]:
                suggestions.append(
                    self.create_item(
                        category=self.DIRECT,
                        label=subtransform_name.title(),
                        short_desc=f'{transform_name} {subtransform_name}',
                        target=f'{transform_name}.{subtransform_name}',
                        args_hint=kp.ItemArgsHint.ACCEPTED,
                        hit_hint=kp.ItemHitHint.KEEPALL)
                )
            self.set_suggestions(suggestions)

    def _build_catalog(self):
        for transform_name, transform in transforms.TRANSFORMS.items():
            if isinstance(transform, dict):  # Nested transforms
                category, args_hint = self.NESTED, kp.ItemArgsHint.REQUIRED
            else:
                category, args_hint = self.DIRECT, kp.ItemArgsHint.ACCEPTED

            yield self.create_item(
                category=category,
                label=transform_name.title(),
                short_desc=f'Converts clipboard into {transform_name}',
                target=transform_name,
                args_hint=args_hint,
                hit_hint=kp.ItemHitHint.NOARGS)
