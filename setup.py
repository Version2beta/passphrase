from distutils.core import setup
import passphrase

setup(
    name='passphrase',
    version='0.1.2',
    author='Rob Martin @version2beta',
    author_email='rob@version2beta.com',
    packages=['passphrase'],
    scripts=[],
    url='http://pypi.python.org/pypi/passphrase/',
    license='LICENSE.txt',
    description='List a series of words for selection of a secure and rememberable passphrase. Choose from many different languages.',
    long_description=open('README.txt').read(),
    install_requires=[],
    package_data={
        '': ['*.dist'],
        'passphrase': ['dictionaries/*.txt'],
      },
    entry_points={
        'console_scripts': [
          'passphrase = passphrase:main',
        ],
      },
)
