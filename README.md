# LeagueofLegends-PatchNote-Scraper

This is a python scraper to get basic information about a League of Legends patch from the [League of Legends patch notes website] (https://www.leagueoflegends.com/en-gb/news/tags/patch-notes/).
The text of the information is transformed into markdown format because i meant to use it for my discord bot.
I may add more information later... or not.
But I'll try to maintain it if it's broken.

# Usage

Simply instantiate `PatchNotes` with the following optional arguments:
..* `previous (int)`: to specifie the patch wanted, from the current one (`0` by default to get the current patch, `1` to get the previous one, etc...)
..** `lang (str)`: the location code to specifie the langage (`en-gb` by default)

During initialisation, the `PatchNote` object will create the following attribu that can be used to get patch informations:
..* `title (str)`: the title of the patch article
..* `description (str)`: the first paragraph of the article
..* `link (str)`: the url of the article
..* `overview_image (str)`: the url overview image of the patch

The url used to make de requests are also store:
..* `menu_request_url (str)`: the url used to get the list of patchs.
..* `patch_request_url (str)`: the url used to get the data of the patch

# requirements

The library neede are:
..* `requests`
..* `bs4`
..* `markdownify`

