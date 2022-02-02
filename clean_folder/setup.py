import setuptools

setuptools.setup(
    name="clean_folder",
    version="0.0.1",
    author="Polina",
    author_email="gtpolina@gmail.com",
    description="Clean folder package",
    #package_dir={"": "clean_folder"},
    packages=setuptools.find_packages(),   
    entry_points = {
        'console_scripts': ['clean-folder=clean_folder.clean:main'],
    }
   
)
