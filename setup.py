from setuptools import setup
setup(name='pylimitbook',
      description='Fast Limit-Order book in python',
      url="https://github.com/abcabhishek/PyLimitOrderBook",
      version='20180103',
      author='Abhishek Chattopadhyay',
      license='MIT',
      packages=['pylimitbook'],
      scripts=['bin/bookViewer.py',
               'bin/create_graphing_data.py',
               'bin/limitbook-convert-csv.py',
               'bin/limitbook-parse.py',
               'bin/limitbook-tseries.py'])
