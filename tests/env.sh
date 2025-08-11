#!/bin/bash

# Test environment variables for envsh library
# Demonstrating variable interpolation - the main advantage over .env files

export TEST_INT=123
export TEST_FLOAT=45.67
export TEST_STR="Hello, World!"
export TEST_BASE_VALUE="base"
export TEST_SPECIAL_CHARS="hello world, test@example.com"

# Variable interpolation in arrays - this is the key advantage!
export TEST_INT_ARRAY="1,$TEST_INT,3,4,5"
export TEST_STR_ARRAY="foo,$TEST_STR,baz"
export TEST_MIXED_INTERPOLATION="prefix-$TEST_BASE_VALUE,value-$TEST_INT,suffix"

# Complex interpolation examples
export TEST_CALCULATED_ARRAY="$TEST_INT,$(($TEST_INT + 10)),$(($TEST_INT * 2))"
export TEST_DYNAMIC_STRING="Generated at $(date +%H:%M)"

export TEST_EMPTY_STR=""
export TEST_EMPTY_ARRAY=""
export TEST_SINGLE_INT="42"
export TEST_SINGLE_STR="single"
export TEST_SPACES_ARRAY="  apple  , banana , cherry  "
export TEST_MIXED_NUMBERS="10,20,30"
