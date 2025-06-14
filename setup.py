from setuptools import setup, find_packages

setup(
    name='dev_ink',
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    entry_points={
        'gui_scripts': [
            'dev_ink = dev_ink.__main__:main'
        ]
    },
)
