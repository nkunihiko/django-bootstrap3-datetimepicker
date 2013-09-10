from setuptools import setup


def read_file(filename):
    # pandoc --from=markdown --to=rst --output=README.rst README.md
    try:
        import os
        path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        file_path = os.path.join(path, filename)
        return open(file_path).read()
    except:
        return ''

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
    'Environment :: Web Environment',
    'Framework :: Django',
]

setup(
    name='django-bootstrap3-datetimepicker',
    packages=['bootstrap3_datetime',],
    version='1.0.1',
    description='Bootstrap3 compatible datetimepicker for Django projects.',
    long_description=read_file('README.rst'),
    author='Nakahara Kunihiko',
    author_email='nakahara.kunihiko@gmail.com',
    url='https://github.com/nkunihiko/django-bootstrap3-datetimepicker',
    license='Apache License 2.0',
    classifiers=CLASSIFIERS,
    include_package_data=True,
    keywords=['datepicker', 'JavaScript', 'DateTimeField', 'DateTimeInput', 'widget'],
)
