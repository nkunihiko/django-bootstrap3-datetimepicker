from setuptools import setup


setup(
    name='django-bootstrap3-datetimepicker',
    packages=['bootstrap3_datetime',],
    package_data={'bootstrap3_datetime': ['static/bootstrap3_datetime/css/*.css', 
                                          'static/bootstrap3_datetime/js/*.js',
                                          'static/bootstrap3_datetime/js/locales/*.js',]},
    include_package_data=True,
    version='2.2.3',
    description='Bootstrap3 compatible datetimepicker for Django projects.',
    long_description=open('README.rst').read(),
    author='Nakahara Kunihiko',
    author_email='nakahara.kunihiko@gmail.com',
    url='https://github.com/nkunihiko/django-bootstrap3-datetimepicker',
    license='Apache License 2.0',
    classifiers=[
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
    ],
)
