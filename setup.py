from setuptools import setup

setup(
	name="edfarm",
	version='1.0',
	description='Earthy Dirt Farm',
	author='Jim Barnes',
	author_email='jimbarnesdeveloper@gmail.com',
	install_requires=[
		'Django==1.8',
		'Pillow==2.8.1',
		'django-widget-tweaks==1.3',
		'wsgiref==0.1.2',
		'python-openid',
		'requests-oauthlib',
		'requests',
		'six',
		'python-social-auth',
	]
)
