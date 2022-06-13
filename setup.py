from distutils.core import setup


setup(
    name='tbdf',
    version="1.0.0",
    author="tokudo",
    author_email="kernel.takato@gmail.com",
    packages=[
        'tbdf'
    ],
    install_requires=[
        "tensorflow>=2.0",
        "pandas>=1.4"
    ]
)