from distutils.core import setup
setup(
  name = 'TOPSIS-Tanishq-101803705',         # How you named your package folder (MyLib)
  packages = ['TOPSIS-Tanishq-101803705'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library to perform the topsis analysis and rank ',   # Give a short description about your library
  author = 'Tanishq Bhalla',                   # Type in your name
  author_email = 'bhalla.tanishq2000@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Tanishq457/TOPSIS-Tanishq-101803705',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Tanishq457/TOPSIS-Tanishq-101803705/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', 'RANK'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'sklearn',
      ],
  long_description="""# Markdown supported!\n\n* Cheer\n* Celebrate\n""",
  long_description_content_type='text/markdown'
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
