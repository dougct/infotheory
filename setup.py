from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='infotheory',
      version='0.1',
      description='Implementations of Information Theory concepts.',
      url='http://github.com/dougct/infotheory',
      author='Douglas Teixeira',
      author_email='',
      license='MIT',
      packages=['infotheory'],
      install_requires=[
        'numpy',
        'pandas',
        'scipy',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)

