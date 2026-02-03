apk update && apk upgrade
pkg update && pkg upgrade
# Update everything
pkg update && pkg upgrade -y
# Install Python and the 'requests' library (for fetching web pages)
pkg install python -y
pip install requests beautifulsoup4
nano scraper.py
