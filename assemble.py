import os
from vdist.builder import Builder
from vdist.source import directory

builder = Builder()

builder.add_build(
    app='vdist-django-example',
    version='1.0',
    source=directory(path=os.getcwd()),
    profile='centos6'
)
builder.build()
