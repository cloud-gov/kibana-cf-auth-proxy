#!/usr/bin/env bash

set -euo pipefail
shopt -s inherit_errexit

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

pushd ${dir}
trap popd exit

cf api ${CF_API_URL}
cf auth 
cf t -o ${CF_ORGANIZATION} -s ${CF_SPACE}

../dev cf-network
