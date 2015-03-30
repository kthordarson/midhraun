from setuptools import setup, find_packages

setup(
    name="midhraun",
    version="0.1",
    url="http://www.midhraun.is",
    license="Proprietary",
    description="Horse stuff",
    author="Heiðar Þórðarson",
    author_email="heidarlitli@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    setup_requires=["setuptools_git"],
    install_requires=["setuptools"],
)
