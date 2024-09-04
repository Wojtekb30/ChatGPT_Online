# ChatGPT_Online
Named by me AlgorytmWeb, this is my solution to give OpenAI's ChatGPT live Internet access. Thanks to that, it can look up latest info online on any topic.

# How does it work:

When the user types in a propt, a instance of ChatGPT-4o-mini writes a web search prompt based on it. Then, it is used to do a web search with Yahoo browser (only one I found a working library for).

From the browser, the program fetches list of URLs and short descriptions.

If set to do so on startup, the program will fetch HTMLs from each of the websites with a GET request. Then, an instance of ChatGPT-4o-mini finds releavent info directly in the HTMLs and summarises it.

Lastly, all inforation gathered from the web gets appeneded to system message of a ChatGPT-4o instance, which then generates the final answer.

# Usage note:

On startup, you have to set fetched webpage limit and True or False for settings such as (simple and weak, based on ChatGPT-3.5-turbo) prompt injection defence, fetching HTMLs of all the individual websites, or always forcing web search (since by default the AI may decide to not search the web, by the ChatGPT-4o-mini which I mentioned the first returning string DONOTSEARCH, which it should in case of greeting and creative requests such as for example writing a song).

# This code and program is part of my Algorytm AI research program.
https://algorytm.birdtech.pl/
