from distutils.core import setup
import py2exe

setup(
    name='WAF_TEST',
    options = {'py2exe':{'bundle_files':1}},
    windows = [{'script': "WAF_TEST.py"}],
    zipfile = None,
    version='1.1',
    packages=[''],
    url='',
    license='',
    author='CHOI MAN-KYUN',
    author_email='mk.choi@piolink.com',
    description=''
)
