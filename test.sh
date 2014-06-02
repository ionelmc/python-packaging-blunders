#!/bin/bash -eEx

rm -rf .ve
virtualenv .ve
source .ve/bin/activate
(
    cd $1
    python setup.py develop
)
test-module
test-package
python -c 'import some_test_junk' || true
python -c 'import setup'

