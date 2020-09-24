"""Tag raw

```liquid
{% raw %} ... {% endraw %}
```
"""
from .manager import tag_manager
from .tag import Tag
from ..exceptions import LiquidSyntaxError

@tag_manager.register
class TagRaw(Tag):
    """The raw tag"""
    RAW = True

    def parse(self, force=False):
        if self.content:
            raise LiquidSyntaxError(
                f"No content allow for tag: {self!r}",
                self.context, self.parser
            )

    def _render(self, local_vars, global_vars):
        return self._render_children(local_vars, global_vars)
