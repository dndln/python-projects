from setuptools import setup

setup(
    name='dice',
    version='0.1',
    py_modules=['dice'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dice=dice:cli
        ''',
)
