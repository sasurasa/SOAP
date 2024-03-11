from setuptools import setup

with open ("README.md") as f:
	long_description = f.read()
setup(name='SURPY',
version='2.0.0',
description='SURPY python for surgical data analysis',
url='https://github.com/sasurasa/',
author='Surasak Sangkhathat',
author_email='s.sangkhathat@gmail.com',
license='Prince of Songkla University',
packages=['SURPY'],
zip_safe=False,
long_description=long_description,
    long_description_content_type='text/markdown'
)