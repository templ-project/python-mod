from pytempl.templ.tools import Base


class Bandit(Base):
    """
    :see: https://github.com/PyCQA/bandit
    """

    TOKEN = 'bandit'

    ORDER = Base.ORDER_LINTER

    CATEGORY = Base.CATEGORY_LINTER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.bandit': 'https://templ-project.github.io/python-configs/.bandit'
            },
            'hook': 'bandit -ini .bandit',
            'name': 'Bandit (https://github.com/PyCQA/bandit)',
            'packages': ['bandit']
        })