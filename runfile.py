from packgram.manage import PythonPackgramModule

class MainModule(PythonPackgramModule):

    #Vars
    
    author = 'roll'
    author_email = 'roll@respect31.com'
    caution = 'DO NOT CHANGE THIS FILE. SOURCE IS IN "_sources" DIRECTORY.'
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.3', 
        'Topic :: Software Development :: Libraries :: Python Modules', 
        'Topic :: System :: Systems Administration', 
    ]
    description = 'Run is a program to run tasks from files.'
    development_requires = ['Sphinx>=1.2'] 
    github_user = 'respect31'
    install_requires = ['box>=0.14']
    license = 'MIT License'  
    maintainer = 'roll'
    maintainer_email = 'roll@respect31.com'
    name = 'run'
    platforms = ['Unix'] 
    pypi_name = 'runpack'
    pypi_user = 'roll'
    pypi_password_secure = 'JaTeiyjnimmtwhbdfPMZZdtp+5S920vb0HobJWL1QQjHVAo5Hwt0kTWYG+zjDrpWUL+NanVNqhQA8xnvWKbI5cZ+n3PvS7KFbgn6XcTYfeEGyEdYUFi0sXaUsgcfke+9nyMBDLoRH2M7TGqpLY2dmXk5C0h0RMkkAPjxgZCan94='
    tests_require = ['nose']
    test_suite = 'nose.collector'    