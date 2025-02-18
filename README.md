# perplexity-cli-cxa
Perplexity AI CLI Client written in Python by Perplexity AI to connect to perplexity.ai API to run queries.

I like to use CLI to interface with LLMs.  Surprisingly, Perplexity does not have their own CLI. (as of: 2025-02-17)

**Status:** Work in Progress

I use MacOS as my daily driver and therefore have primarily focused on making this work on MacOS first.  This may work with Linux, also.

I just discovered there is a "perplexityClient Python module.

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

**Note/Tip** - I do not like to simply set ENV variables with sensitive data directly in my shell/terminal (as it leaves a trail in .bash_history that could potentially be scraped)

You can add the following to any text file (I choose to use one of my ".bashrc" files
```bash
echo 'export PERPLEXITY_API_KEY="blah"' | tee -a myenvfile
source myenvfile
```

## Create CLI script using prompt with Claude (did not work, but leaving as a reference)
```bash
You are a data engineer.  Please write a python script to connect to perplexity.ai from the macos bash shell.  The script should accept parameters 1/ list available models using '-l' 2/ use a specific model using '-m' or '--model'.  The script should read the environment variable 'PERPLEXITY_API_KEY'.  It should also accept a '-h' or '--help' to return syntax examples"
```

## Create CLI script using prompt with Perplexity (did work)

```bash
Help me write a python to script to do the following:
reference an ENV variable PERPLEXITY_API_KEY 
make a call to the perplexity AI API endpoint
-t to set the maximum number of tokens
-m to set the model to use for the query
-h to display help for this script
-l to list available models
create separate variables for the different parts of the API results and then print each part with a header.
```
-- Note:  the genAI created script opted to accept a '-q' for the prompt query, which I am cool with.

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

### Example with output
```bash
$ ./perplexity-cli-cxa-working.py -m sonar-pro -q "What is the distance between the Sun and Earth?"

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

## TODO
* I need to learn how/when/where to attribute other work that I use.  An example: much of the actual script was created by perplexity.ai - should I provide attribution?  If so, where?
* I would probably like to clean up the output returned by the API.  Currently (2025-02-17) the API call resturns a wide array of outputs.  

## References

The resulting script [perplexity-cli-cxa.py](./perplexity-cli-cxa.py) was generated with assistance from Perplexity AI. 
