# perplexity-cli-cxa
Perplexity AI CLI Client written in Python by Perplexity

Status: Work in Progress

I will begin working on this script to work on MacOS.  It may work the same on Linux, but I will not focus my efforts there at this time.

## Prerequisites
You need to retrieve your API Key from Perplexity.ai  
Prompt `where do I retrieve my Perplexity.ai API Key?`

<pre>
To retrieve your Perplexity.ai API Key, follow these steps:
1.	Log in to your Perplexity account at www.perplexity.ai.
2.	Navigate to the Settings page, usually located in the bottom left corner of the interface.
3.	Click on the “API” tab in the settings menu.
4.	In the API tab, you can either copy your current API key or generate a new one by clicking the “Generate” button.

Remember to keep your API key secure and treat it like a password. The API key is a long-lived access token that you can use until you manually refresh or delete it.
</pre>

Now - I do not simply like to set ENV variables at the command line (as it leaves a trail in .bash_history that could potentially be scraped)

You can add the following to any text file (I choose to use one of my ".bashrc" files
```bash
echo 'export PERPLEXITY_API_KEY="blah"' | tee -a myenvfile
source myenvfile
```

## Prompt
```bash
You are a data engineer.  Please write a python script to connect to perplexity.ai from the macos bash shell.  The script should accept parameters 1/ list available models using '-l' 2/ use a specific model using '-m' or '--model'.  The script should read the environment variable 'PERPLEXITY_API_KEY'.  It should also accept a '-h' or '--help' to return syntax examples"
```

To use this script:
1.	Save it as `perplexity_cli.py` and make it executable with `chmod +x perplexity_cli.py`.
2.	Set your Perplexity API key as an environment variable:

```bash
export PERPLEXITY_API_KEY="your_api_key_here"
```


3.	Run the script with different options:
•	To list available models:
```bash
./perplexity_cli.py -l
```

•	To use a specific model:
```bash
./perplexity_cli.py -m model_name -p "Your prompt here"
```

•	To display help information:
```bash
./perplexity_cli.py -h
```

This script uses the OpenAI client library, which is compatible with the Perplexity API. It reads the API key from the environment variable, lists available models, and allows you to use a specific model with a given prompt. The help option provides syntax examples for using the script.
