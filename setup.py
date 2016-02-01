from distutils.core import setup
setup(
  name = 'lowendspirit',
  packages = ['lowendspirit'], # this must be the same as the name above
  version = '0.1',
  description = 'Library to call endpoints of API's for CloudFlare, SolusVM and Virtualizor ',
  author = 'Damir H.',
  license = 'MIT',
  author_email = 'info@boxcontrol.net',
  url = 'https://github.com/boxcontrol/lowendspirit', 
  download_url = 'https://github.com/boxcontrol/lowendspirit/tarball/0.1', 
  keywords = ['virtualizor', 'solusvm', 'lowendspirit', 'cloudflare', 'API', 'enduser'], # arbitrary keywords
  classifiers = [
		"Development Status :: 3 - Alpha,
		"Intended Audience :: Developers",
    		"Natural Language :: English",
		"Operating System :: OS Independent",
    		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
    		"Programming Language :: Python :: 3.3",
    		"Programming Language :: Python :: 3.4",
    		"Programming Language :: Python :: 3.5",
		],
)