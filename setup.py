if __name__ == '__main__':
    from setuptools import setup
    from displot.displot import displotInfo

    with open("README.md", 'r') as f:
        long_description = f.read()

    setup(
       name=displotInfo['appTitle'],
       version=displotInfo['appVersion'],
       description='Structural dislocation detector.',
       long_description=long_description,
       license="GPLv3",
       author='Bohdan Starosta',
       author_email='bjstarosta@gmail.com',
       packages=['displot'],
       install_requires=[
        'numpy',
        'scipy',
        'scikit-image'
        ],
    )
