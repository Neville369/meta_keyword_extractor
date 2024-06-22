# meta_keyword_extractor
This Python script reads a list of URLs from a text file and prints the meta keywords of each webpage. Here's a detailed description:

1. **Importing Libraries**:
   - `BeautifulSoup` from the `bs4` library for parsing HTML content.
   - `requests` for making HTTP requests.
   - `lxml` for HTML parsing.
   - `re` for regular expression operations (though it isn't used in the provided code).

2. **Reading URLs from a Text File**:
   - The script opens a file named `urls.txt` in read mode.
   - It reads each line, strips leading/trailing whitespace, and removes any trailing commas.
   - The processed URLs are stored in a list named `urls`.

3. **Defining a Function to Get the Meta Keywords of a Webpage**:
   - The `get_keywords` function takes a URL as input.
   - It sends an HTTP GET request to the URL.
   - If the request is successful, it parses the HTML content using `BeautifulSoup` with the `lxml` parser.
   - It searches for the `<meta>` tag with the attribute `name="keywords"`.
   - If the `<meta>` tag is found, it extracts and returns the content of the `content` attribute (the keywords).
   - If the `<meta>` tag is not found or an exception occurs during the request (e.g., network issues, invalid URL), it returns an empty string.

4. **Iterating Over the URLs and Printing Meta Keywords**:
   - The script iterates through each URL in the `urls` list.
   - For each URL, it calls the `get_keywords` function.
   - It prints the keywords of the webpage, prefixed with the URL.

This script is useful for extracting and displaying the meta keywords of multiple webpages, which can be helpful for SEO analysis or content categorization tasks.
