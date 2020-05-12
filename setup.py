import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pysolana',
    version='0.2.0',
    author='Sedov Daniel',
    author_email='danielsedovzzz@gmail.com',
    description='Python Solana Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Gusarich/pysolana',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
