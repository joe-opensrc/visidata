'''
Hello world minimal plugin.  Press F2 to show options.hello_world on the status line.

.visidatarc: `import plugins.hello`
'''

__author__ = 'Paul Swanson <paulsw@example.com>'
__version__ = '1.0'

from visidata import vd, BaseSheet

vd.option('hello_world', '¡Hola mundo!', 'shown by the hello-world command')

BaseSheet.addCommand('KEY_F(2)', 'hello-world', 'status(options.hello_world)')
