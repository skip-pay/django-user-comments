from setuptools import setup, find_packages

setup(
    name='skip-django-user-comments',
    version='0.1.0',
    description='Library for adding comments of users related with object',
    author='Lubos Matl',
    author_email='matllubos@gmail.com',
    packages=find_packages(),
    install_requires=[
        'skip-django-chamber>=0.7.2',
    ],
    include_package_data=True,
    zip_safe=False,
)
