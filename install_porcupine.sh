#!/bin/bash
#
# Project Porcupine install
# Version : Alpha
#

## Global variables
USER="Porcupine"
ROOT="/home/${USER}/Porcupine"

## Install Log file & folder
LOG_DIR="/var/log/porcupine"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/porcupine_install_$(date +%Y-%m-%d-%H-%M-%S).log"

## build out folder structure
echo "Making root folder..."
mkdir -p "$ROOT"
DB="${ROOT}/db"
echo "Making db folder..."
mkdir -p $DB
DB_ARCHIVE="${DB}/archive"
echo "Making db archive folder..."
mkdir -p $DB_ARCHIVE
LIB="${ROOT}/lib"
echo "Making lib folder..."
mkdir -p $LIB
PIC="${ROOT}/pic"
echo "Making pic folder..."
mkdir -p $PIC


