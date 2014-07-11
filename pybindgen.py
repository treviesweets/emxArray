# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os
import sys
import pybindgen
from pybindgen import FileCodeSink
from pybindgen.gccxmlparser import ModuleParser

# <codecell>

def module_gen():
    os.chdir('/home/trevorsweetnam/Dropbox/notebooks/eef/emxarr/codegen/dll/emx_test')
    #module_parser = ModuleParser('emx_test_emxAPI', '::')
    #module = module_parser.parse(['emx_test_emxAPI.h'])
    #module.add_include('"emx_test_emxAPI.h"')
    
    module_parser = ModuleParser('emx_test', '::')
    module = module_parser.parse(['emx_test.h'])
    module.add_include('"rt_noninfite.h"')
    module.add_include('"emx_test_emxutil.h"')
    
    pybindgen.write_preamble(FileCodeSink(sys.stdout))
    module.generate(FileCodeSink(sys.stdout))

# <codecell>

module_gen()

# <codecell>


# <codecell>

cd /home/trevors/Dropbox/notebooks/eef/c/

# <codecell>

ls

# <codecell>


