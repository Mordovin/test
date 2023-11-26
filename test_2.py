import hashlib


class MarsURLEncoder:

    dictionary: dict = {}

    def init(self):
        self.dictionary = {}

    def encode(self, long_url):
        char_length = 8
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        if char_length > 128:
            raise ValueError("char_length {} exceeds 128".format(char_length))
        hash_object = hashlib.sha512(long_url.encode())
        hash_hex = hash_object.hexdigest()
        key = hash_hex[0:char_length]
        value = long_url
        sort_link = 'https://ma.rs/' + key
        self.dictionary = {key: value}
        return sort_link

        # return full_link

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        short_url = short_url.split('.rs/')
        for hesh_url in self.dictionary:
            if hesh_url == short_url[1]:
                return (self.dictionary[short_url[1]])


link = MarsURLEncoder()
print(link.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))
print(link.decode('https://ma.rs/e78dc361'))
print(link.encode('https://tsup.ru/mars/marsohod-1/01-22-2023/daily_job.html'))
print(link.decode('https://ma.rs/2e811edd'))
print(MarsURLEncoder.dictionary)
