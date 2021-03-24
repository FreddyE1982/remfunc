#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from distutils.core import setup
setup(
  name = 'remfunc',         # How you named your package folder (MyLib)
  packages = ['remfunc'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GNU',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Ever needed a python module on a system where you can only install pure python libs, for example Pythonista for IOS? This is a workaround you can use if you have a webserver (or computer reachable over the internet). You run the remfunc server part on your computer and in Pythonista you create an instance of the client and use it to send code to the server which gets executed there and the result returned. Yeah! Now you can use pandas in Pythonista!',   # Give a short description about your library
  author = 'Frederik Egger',                   # Type in your name
  author_email = 'frederik.egger@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/FreddyE1982/remfunc-python',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['python', 'pythonista', 'modules'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

