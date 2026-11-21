
def markdown_to_blocks(markdown):
    results = []
    split_doc = markdown.split("\n\n")

    for result in split_doc:
        result = result.strip()

        if result != "":
            results.append(result)

    return results
