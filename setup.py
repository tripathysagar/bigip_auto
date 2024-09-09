from setuptools import setup, find_packages

# Read dependencies from requirements.txt
def get_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f if line.strip()]

setup(
    name="bigip_project",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files like images if necessary
    install_requires=get_requirements(),  # Dependencies from requirements.txt
    entry_points={
        'console_scripts': [
            # This creates the alias for running the big function
            'bigip=bigip.bigip:main',  # Alias 'bigip' will run the 'big' function from bigip.py
        ],
    },
)


