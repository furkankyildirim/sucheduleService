from setuptools import setup

setup(
    name="SUchedule_Service",
    version="1.0.0",
    maintainer="Furkan K. Yıldırım",
    maintainer_email="contact@furkankyildirim.com",
    packages=['SUchedule_Service'],
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"]
)