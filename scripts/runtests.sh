#!/bin/bash
export SQLALCHEMY_SILENCE_UBER_WARNING=1
rm -rf .env
cp .env.prod .env && pytest $1