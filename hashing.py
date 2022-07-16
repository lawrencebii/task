def get_hash_value(string: str, salt: int):

    original_hash = salt

    for char in string.strip():

        new_hash = ord(char) + (31*original_hash)
        original_hash += new_hash
    print(original_hash)
    return original_hash


get_hash_value('Hello, World', 11)

get_hash_value('a', 0)
