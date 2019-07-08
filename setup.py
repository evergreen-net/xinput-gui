from distutils.core import setup

setup(
    name='xinput-gui',
    version='0.1.0',
    description='A simple GUI for Xorg\'s Xinput tool.',
    author='Ivan Fonseca',
    author_email='ivanfon@riseup.net',
    url='https://github.com/IvanFon/xinput-gui',
    license='GPL3',
    scripts=['xinput-gui'],
    data_files=[('share/xinput-gui', ['app.glade'])]
)
