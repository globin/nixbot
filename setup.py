import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'flask',
    'flask_migrate',
    'flask_sqlalchemy',
    'PyGithub',
    'celery',
    #'flower',
    'redis',
    'requests',
]

tests_require = [
  'pylint', 'mypy', 'pycodestyle',

  'setuptools_scm', 'pytest-runner',  # FIXME needed for pypi2nix
]

setup(name='nixborg',
      version='0.0',
      description='nixborg',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      entry_points={
          'console_scripts': [
              'nixborg-receiver = nixborg.receiver:main',
          ]
      },
      author='',
      author_email='',
      url='',
      keywords='web',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      )
