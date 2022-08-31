#!/bin/bash
# Script to run at build time on vercel

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput