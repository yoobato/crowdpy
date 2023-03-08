import setuptools

with open('./README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='crowdpy',
    version='1.2.3',

    author='Daeyeol Ryu',
    author_email='yoobato@gmail.com',

    license='Apache-2.0',

    description='A Python library for Atlassian Crowd REST API',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/yoobato/crowdpy',

    py_modules=['crowd'],
    python_requires='>=3.9',
    install_requires=['requests'],

    keywords= ['atlassian', 'crowd'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ]
)
