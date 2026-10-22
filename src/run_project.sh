#!/bin/bash
# run_project.sh - Execution script for Horizon OS compilation workspace

# Terminate immediately if error occurs
set -e

echo "🚀 Step 1: Running Python code generator..."
python3 generate_project.py

echo "📦 Step 2: Validating local environment dependencies..."
if ! command -v nasm &> /dev/null || ! command -v g++ &> /dev/null; then
    echo "⚠️ System dependencies missing. Installing compilation toolchains..."
    sudo apt update && sudo apt install -y build-essential nasm qemu-system-x86
fi

echo "🏗️ Step 3: Compiling Horizon OS and Horizon Store architecture..."
make all

echo "🖥️ Step 4: Testing Horizon Store UI Execution..."
./horizon_store

echo "⚙️ Step 5: Testing Compatibility Layer Router..."
./horizon_subsystem

echo "========================================================="
echo "✅ Compilation Complete! To run the actual bootable OS"
echo "   inside QEMU emulation mode, execute: 'make run-kernel'"
echo "========================================================="
