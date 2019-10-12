from distutils.core import setup

setup(name='lawerapp',
      version='1.0',
      description='Python webapplication',
      author='BAC',
      author_email='mrbacco@outlook.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['Flask==1.1.1', 'Flask-Login==0.4.1', 
                'Flask-Mail==0.9.1', 'Jinja2==2.10.1', 'lxml==4.4.1', 
                'passlib==1.7.1', 'pymongo==3.9.0', 
                'urllib3==1.25.3',
                'WTForms==2.2.1'])

