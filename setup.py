from distutils.core import setup

setup(
    name='django-uniflag',
    version='0.1',
    packages=['uniflag', 'uniflag.templatetags'],
    url='https://github.com/dmzio/django-uniflag',
    license='GPLv2',
    author='Dmitry Ziolkovskiy',
    author_email='ziodmitry@gmail.com',
    description='Unified flags for content in Django',
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPLv2",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
