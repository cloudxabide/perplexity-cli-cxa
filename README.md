# perplexity-cli-cxa
Perplexity AI CLI Client written in Python by Perplexity AI to connect to perplexity.ai API to run queries.

With this script and a Perplexity.ai API key, you can run queries.

## Prerequisites
You need to retrieve your API Key from Perplexity.ai    
**Prompt:**  `where do I retrieve my Perplexity.ai API Key?`

<pre>
To retrieve your Perplexity.ai API Key, follow these steps:
1.	Log in to your Perplexity account at www.perplexity.ai.
2.	Navigate to the Settings page, usually located in the bottom left corner of the interface.
3.	Click on the “API” tab in the settings menu.
4.	In the API tab, you can either copy your current API key or generate a new one by clicking the “Generate” button.

Remember to keep your API key secure and treat it like a password. The API key is a long-lived access token that you can use until you manually refresh or delete it.
</pre>

-- **Note/Tip:**   
I do not like to simply set ENV variables with sensitive data directly in my shell/terminal (as it leaves a trail in .bash_history that could potentially be scraped)

You can add the following to any text file (I choose to use one of my ".bashrc" files)
```bash
$ vi ~/.bashrc.d/myperplexkey
export PERPLEXITY_API_KEY="blah"

$ source ~/.bashrc.d/myperplexkey
```

## Create CLI script using prompt with Perplexity 
To create my script, I provided the following prompt to the Perxplexity.ai App
```bash
Help me write a python to script to do the following:
reference an ENV variable PERPLEXITY_API_KEY 
make a call to the perplexity AI API endpoint
-t to set the maximum number of tokens
-m to set the model to use for the query
-l to list available models
create separate variables for the different parts of the API results and then print each part with a header.
```
-- **Note(s):**  
- The genAI created script output proposed to o accept a '-q' for the prompt query, which I am cool with.
- I do not inlcude "-h to display help for this script" in my prompt as python will complain when executed.

To use this script:
1.	Save it as `perplexity_cli_cxa` and make it executable with `chmod +x perplexity_cli_cxa`.
2.	Set your Perplexity API key as an environment variable:

```bash
export PERPLEXITY_API_KEY="your_api_key_here"
```
### Install script in to a common directory (optional)
```bash
sudo install -m 0755 perplexity_cli_cxa /usr/local/bin
```


3.	Run the script with different options:  
•	To list available models:
```bash
./perplexity_cli_cxa -l
```

•	To use a specific model:
```bash
./perplexity_cli_cxa -m model_name -q "Your prompt here"
```

•	To display help information:
```bash
./perplexity_cli_cxa -h
```

### Example with output
**Prompt (at command line)**
```bash
./perplexity_cli_cxa -m sonar-pro -q "What is the distance between the Sun and Earth?"
```

**Results**
```bash
--- Model Used ---
sonar-pro

--- Choices ---
Message: The average distance between the Sun and Earth is approximately 93 million miles (150 million kilometers)[1][4]. This distance is also defined as 1 Astronomical Unit (AU)[4].

However, it's important to note that Earth's orbit around the Sun is not perfectly circular, but slightly elliptical. This means the actual distance varies throughout the year:

1. At its closest point (perihelion), Earth is about 91.4 million miles

--- Usage ---
prompt_tokens: 16
completion_tokens: 100
total_tokens: 116
citation_tokens: 5204
num_search_queries: 1
```

## Status, Notes, References
I like to use CLI to interface with LLMs.  Surprisingly, Perplexity does not have their own CLI. (as of: 2025-02-17)

**Status:** Work in Progress

I use MacOS as my daily driver and therefore have primarily focused on making this work on MacOS first.  This may work with Linux, also.

I just discovered there is a "perplexityClient Python module.

### TODO
* I need to learn how/when/where to attribute other work that I use.  An example: much of the actual script was created by perplexity.ai - should I provide attribution?  If so, where?
* I would probably like to clean up the output returned by the API.  Currently (2025-02-17) the API call resturns a wide array of outputs.  

### References
[Perplexity AI - Getting Started](https://docs.perplexity.ai/guides/getting-started)  

The resulting script [perplexity_cli_cxa](./perplexity_cli_cxa) was generated with assistance from Perplexity AI. 

### Create CLI script using prompt with Claude (did not work, but leaving as a reference)
I provided the following prompt to the Perxplexity.ai App
<pre>
You are a data engineer.
Please write a python script to connect to perplexity.ai from the macos bash shell.
The script should accept parameters 1/ list available models using '-l' 2/ use a specific model using '-m' or '--model'.
The script should read the environment variable 'PERPLEXITY_API_KEY'.
It should also accept a '-h' or '--help' to return syntax examples"
</pre>

### Notes

The original script name was "perplexity_cli.py" which I changed to perplexity_cli_cxa - as I assume there will be many perplexity_cli.py out in the wild.

> Is it possible to query what LLMS are available for use with perxplexity.ai using an API call?
```
Yes, it is possible to query which LLMs are available for use with Perplexity’s API. The pplx-api allows developers to specify the model they want to use in their requests. However, there is no direct API endpoint explicitly designed to list all available models dynamically. Instead, developers must refer to documentation or announcements to know which models are supported.
```
