@echo off
FOR /L %%s IN (1, 2, 880) DO (
	python scrapingAO3.py %%s
	timeout /t 720 /nobreak > NUL
)
