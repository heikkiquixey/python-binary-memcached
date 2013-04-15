from setuptools import setup
setup(
    name='python-binary-memcached',
    version='0.17',
    author='Jayson Reis',
    author_email='santosdosreis@gmail.com',
    description='A pure python module to access memcached via it\'s binary' +
                ' protocol with SASL auth support',
    url='https://github.com/jaysonsantos/python-binary-memcached',
    packages=['bmemcached'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)