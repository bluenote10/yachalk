#!/usr/bin/env python

import setuptools  # type: ignore

if __name__ == "__main__":
    setuptools.setup(
        package_data={
            "yachalk": ["py.typed"],
        }
    )
