# Etherscan_Scrapper
A scrapy pyhton project to crawl https://etherscan.io/ and collect all the solidity files for analysis

Steps: 
1. pip install scrapy
2. scrapy startproject "project_name"
3. Set USER_AGENT='to some browser agent' (example: 'Mozilla/5.0 (Linux; Android 6.0; vivo 1601 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36'). Set DOWNLOAD_DELAY=9 in settings.py of your created project

3. copy etherscrapper.py, codescrapper.py  and solcreator.py inside spiders directory of your project

4. Run: scrapy crawl EtherScan_Spider -o contents.json

5. Run: scrapy crawl code_spider -o codeoutput.json

6. Run: mkdir solidityFiles

7. Run: python solcreator.py


You will have the crawled solidity files saved in the soldityFiles directory
