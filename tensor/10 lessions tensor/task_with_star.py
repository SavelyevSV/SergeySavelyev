# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
    # Здесь пишем код
def test(request):
    marker = request.node.get_closest_marker('id_check')
    arguments = marker.args
    print('\n', *arguments)
