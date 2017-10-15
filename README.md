# Thesis Progress Monitor

Create a bot which can monitor the progress of your paper

## USAGE

### Get Your Twitter API

1. You need to get twitter api access keys
   1. Open https://apps.twitter.com/ 
   2. Click **Create New App**
   3. Fill out info (Note: Website URL should be filled out. I recommend `127.0.0.1`)
   4. Click **Create your Twitter application**
   5. Go to the next step!

2. Set those access keys in `monitor.py`
```python
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_SECRET_ACCESS_TOKEN"
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_API_KEY"
```

### Post Your Progress on Twitter

You need to make a directory and file to save **your progress log**
```shell
$ cd thesis-progress-monitor
$ chmod 700 init.sh
$ ./init.sh
```

Set your parameters in `monitor.py`
```python
log_file_path = 'YOUR_LOG_PATH'
pdf_file_path = 'YOUR_PDF_PATH'
your_name = 'YOUR_NAME'
your_thesis_type = 'YOUR_THESIS_TYPE'
```

Post your progress on twitter!!
```shell
$ python monitor.py
```

### Monitor Your Progress
Turn on `crontab` and monitor your progress

1. On the terminal, run the command 
```shell
$ crontab -e
```

2. On the editor, write the code as bellow
```
MAILTO='YOUR_EMAIL_ADRESS' # or "" not to send e-mail
* * */1 * * python your/absolute/path/to/thesis-progress-monitor/monitor.py
```

3. To check what you wrote, run the command
```shell
$ crontab -l
```
