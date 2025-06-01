from setuptools import setup

setup(
    name='Dev Ink',
    version='1.0.0',
    packages=['dev_ink'],
    entry_points={
        'gui_scripts': [
            'dev_ink = dev_ink.__main__:main'
        ],
    },
)
