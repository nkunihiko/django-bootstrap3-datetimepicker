from setuptools import setup
import os


def read_file(filename):
    try:
        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
        return open(filepath).read()
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
    version='1.0.0',
    description='bootstrap-datetimepicker for Django projects',
    long_description=read_file("README.md"),
    author='Nakahara Kunihiko',
    author_email='nakahara.kunihiko@gmail.com',
    url='https://github.com/nkunihiko/django-bootstrap3-datetimepicker',
    license='Apache License 2.0',
    classifiers=CLASSIFIERS,
    include_package_data=True,
    keywords=['datepicker', 'JavaScript', 'DateTimeField', 'DateTimeInput', 'widget'],
)
