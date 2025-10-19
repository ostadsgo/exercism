def response(hey_bob: str):

    hey_bob = hey_bob.strip()

    if hey_bob.endswith("?") and not hey_bob.isupper():
        return "Sure."
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if  hey_bob in "\t\n\r ":
        return "Fine. Be that way!"
    return "Whatever."



