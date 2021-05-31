# this example is in pypro folder

# Create .txt file
    # Create compression file (.py)
      # This is so we can write code to go through the data to compress it
      # We need to use data = open('txt file name','r').read()
        # To check that we can read our data use print(data)
        # Run it with python3 compress.py

    # To compress, import zlib to use the compress method
        # replace print with zlib.compress(data)
        # convert data to bytes to avoid errors due to string
        # between data and zlib use compressed data bytes(data,'utf-8')
        # we also need to import base64  which helps us encode data
            # this way we can use the methode base64.b64encode() and pass our zlib method into it

    # To write a compressed data to a file
        # First decode data to write it to new file
        # Then write it to a new file with open() and .write()

# DECOMPRESSION
    # using zlib.decompress(base64.b64decode(variable name)) will decode then decompress data (reverse of compressing it
