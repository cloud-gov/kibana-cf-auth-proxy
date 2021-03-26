#!/usr/bin/env bash

set -euo pipefail
shopt -s inherit_errexit

src/dev set-up-environment
bandit -r kibana_cf_auth_proxy
src/dev test
