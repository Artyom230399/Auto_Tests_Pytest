import pytest

from Rating_Generator.Generator import rating_generator


@pytest.mark.parametrize("cond, exp", [
    (0, 'На экзамен не явился')
])
