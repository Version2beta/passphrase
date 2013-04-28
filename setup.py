from distutils.core import setup

setup(
    name='passphrase',
    version='0.0.2',
    author='Rob Martin @version2beta',
    author_email='rob@version2beta.com',
    packages=['passphrase'],
    scripts=[],
    url='http://pypi.python.org/pypi/passphrase/',
    license='LICENSE.txt',
    description='List a series of words for selection of a secure and rememberable passphrase.',
    long_description=open('README.md').read(),
    install_requires=[],
    package_data={
        '': ['*.dist'],
      },
    entry_points={
        'console_scripts': [
          'passphrase = passphrase:main',
        ],
      },
)
