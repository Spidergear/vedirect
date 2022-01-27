from setuptools import setup

setup(name='vedirect',
      version='0.1',
      description='Victron VE.Direct decoder for Python',
      url='https://github.com/Spidergear/vedirect',
      author='Dieter Lubbe',
      author_email='DieterLubbe@gmail.com',
      license='MIT',
      packages=['vedirect'],
      install_requires=[
          'pyserial',
      ],
      zip_safe=False)
