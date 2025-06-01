from setuptools import setup, find_packages

setup(
    name='dev_ink',
    version='0.9.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'dev_ink = dev_ink.__main__:main'
        ]
    },
)
