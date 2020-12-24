# [`angelogladding.com`][1] Copyright @[Angelo Gladding][2] 2020-
#
# This program is free software: it is distributed in the hope that it
# will be useful, but *without any warranty*; without even the implied
# warranty of merchantability or fitness for a particular purpose. You
# can redistribute it and/or modify it under the terms of the @@[GNU's
# Not Unix][3] %[Affero General Public License][4] as published by the
# @@[Free Software Foundation][5], either version 3 of the License, or
# any later version.
#
# *[GNU]: GNU's Not Unix
#
# [1]: https://github.com/angelogladding/angelogladding
# [2]: https://angelogladding.com
# [3]: https://gnu.org
# [4]: https://gnu.org/licenses/agpl
# [5]: https://fsf.org

"""Angelo Gladding's canopy instance."""

from setuptools import setup

setup(requires=["canopy"],
      provides={"web.apps": ["angelogladding = canopy:app"]},
      discover=__file__)
