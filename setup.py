import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip


setup(
    cmdclass={'sdist': sdist_upip.sdist},
    name='circuitpython-hx711',
    py_modules=['hx711'],
    version='0.1',
    description='Circuitpython driver for the HX711',
    long_description='Circuitpython driver for the HX711 24-Bit Analog-to-Digital Converter',
    keywords=['circuitpython', 'hx711'],
    url='https://github.com/bunderuso/circuitpython-hx711',
    author='Bunderuso',
    maintainer='Bunderuso',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: Implementation :: CircuitPython',
        'License :: OSI Approved :: MIT License',
    ],
)
