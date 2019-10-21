import foo                 # foo imported and bound locally
# below three statements imports foo.bar.baz
import foo.bar.baz         # foo bound locally
import foo.bar.baz as fbb  # foo.bar.baz bound as fbb
from foo.bar import baz    # foo.bar.baz bound as baz
from foo import attr  # foo imported, foo.attr bound as attr
