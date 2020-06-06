from setuptools import setup
from pathlib import Path

requirements = Path('requirements.txt').read_text().split('\n')
readme = Path('README.md').read_text()


setup(name="cacheit",
      version="0.0.3",
      description="Caching decorator based on cache-tools",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://alexdelorenzo.dev",
      author="Alex DeLorenzo",
      license="AGPL-3.0",
      packages=['cacheit'],
      zip_safe=True,
      install_requires=requirements,
       keywords="caching decorator cache-tools".split(' '),
     # entry_points={"console_scripts":
     #                   ["campfs = campfs.command:cmd"]},
      python_requires='~=3.7',
)
