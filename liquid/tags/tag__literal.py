"""The literal tag"""
from .manager import tag_manager
from .tag import Tag
from ..utils import logger
from ..config import LIQUID_LOG_INDENT

@tag_manager.register
class TagLITERAL(Tag):
    """The literal tag"""
    VOID = True

    def _render(self, local_vars, global_vars):
        # pylint: disable=unused-argument
        content = self.content
        if self.open_compact:
            content = content.lstrip()
        if self.close_compact:
            content = content.rstrip()
        return content

    def render(self, local_vars, global_vars, from_elder=False):
        logger.debug('[dim italic]%s  Rendering %r[/dim italic]',
                     (self.context.level) * LIQUID_LOG_INDENT,
                     self,
                     extra={"markup": True})
        return str(self._render(local_vars, global_vars)), local_vars
