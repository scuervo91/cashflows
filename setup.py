import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cashflows2", # Replace with your own username
    version="v0.0.1",
    author="Juan D. Velasquez & Ibeth K. Vergara. Forked Santiago Cuervo",
    author_email="scuervo91@gmail.com",
    description="'Investment modeling and advanced engineering economics using Python'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='cashflow investments bonds depreciation loan irr',
    url="https://github.com/scuervo91/cashflows2",
    download_url="https://github.com/scuervo91/cashflows2/archive/v0.0.1.tar.gz",
    packages=setuptools.find_packages(),
    include_package_data = True,
    package_data = {'':['*.csv','*.json']},
    install_requires=[            
        'numpy',
        'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
